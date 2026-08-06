from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from users.model import User
from users.services import get_current_user
from . import schema, services

router = APIRouter()


@router.post("/", response_model=schema.FeedbackRead, status_code=status.HTTP_201_CREATED)
def create_feedback(
    data: schema.FeedbackCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return services.create_feedback(db, current_user.user_id, data)


@router.get("/me", response_model=list[schema.FeedbackRead])
def get_my_feedbacks(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return services.get_user_feedbacks(db, current_user.user_id)
