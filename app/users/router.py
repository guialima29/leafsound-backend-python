from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.orm import Session

from database import get_db
from rate_limit import limiter
from . import schema, services
from .model import User

router = APIRouter()
auth_router = APIRouter()


@auth_router.post("/google", response_model=schema.TokenResponse)
@limiter.limit("10/minute")
def login_with_google(request: Request, data: schema.GoogleLoginRequest, db: Session = Depends(get_db)):
    access_token, user = services.login_with_google(db, data.id_token)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user,
    }


@auth_router.post("/dev-login", response_model=schema.TokenResponse)
@limiter.limit("10/minute")
def login_for_development(request: Request, data: schema.DevLoginRequest, db: Session = Depends(get_db)):
    access_token, user = services.login_for_development(db, data)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user,
    }


@router.get("/me", response_model=schema.UserRead)
def get_me(current_user: User = Depends(services.get_current_user)):
    return current_user


@router.patch("/me", response_model=schema.UserRead)
def update_me(
    data: schema.UserUpdate,
    current_user: User = Depends(services.get_current_user),
    db: Session = Depends(get_db),
):
    return services.update_user(db, current_user, data)


@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
def delete_me(
    current_user: User = Depends(services.get_current_user),
    db: Session = Depends(get_db),
):
    services.delete_user(db, current_user)
