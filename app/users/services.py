import os
import uuid

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from database import get_db
from . import auth, schema
from .model import User

bearer_scheme = HTTPBearer(auto_error=False)


def get_user_by_id(db: Session, user_id: uuid.UUID) -> User | None:
    return db.query(User).filter(User.user_id == user_id).first()


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.user_email == email).first()


def get_user_by_google_sub(db: Session, google_sub: str) -> User | None:
    return db.query(User).filter(User.google_sub == google_sub).first()


def login_with_google(db: Session, id_token: str) -> tuple[str, User]:
    google_data = auth.verify_google_token(id_token)
    user = get_user_by_google_sub(db, google_data["sub"])

    if not user:
        user = get_user_by_email(db, google_data["email"])

    if user:
        user.google_sub = google_data["sub"]
        user.user_name = google_data.get("name") or user.user_name
        user.avatar_url = google_data.get("picture")
    else:
        user = User(
            user_name=google_data.get("name") or google_data["email"].split("@")[0],
            user_email=google_data["email"],
            google_sub=google_data["sub"],
            avatar_url=google_data.get("picture"),
        )
        db.add(user)

    db.commit()
    db.refresh(user)

    return auth.create_access_token(str(user.user_id)), user


def login_for_development(db: Session, data: schema.DevLoginRequest) -> tuple[str, User]:
    if os.getenv("APP_ENV") != "development":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Development login is disabled",
        )

    user = get_user_by_email(db, data.user_email)

    if user:
        user.user_name = data.user_name
        user.avatar_url = data.avatar_url
    else:
        user = User(
            user_name=data.user_name,
            user_email=data.user_email,
            google_sub=f"dev:{data.user_email}",
            avatar_url=data.avatar_url,
        )
        db.add(user)

    db.commit()
    db.refresh(user)

    return auth.create_access_token(str(user.user_id)), user


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> User:
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication token required",
        )

    payload = auth.decode_access_token(credentials.credentials)
    try:
        user_id = uuid.UUID(payload["sub"])
    except (KeyError, ValueError) as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
        ) from exc

    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authenticated user not found",
        )

    return user


def update_user(db: Session, user: User, data: schema.UserUpdate) -> User:
    user.user_name = data.user_name
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user: User) -> None:
    db.delete(user)
    db.commit()
