import uuid

from sqlalchemy.orm import Session

from . import schema
from .model import Feedback


def create_feedback(
    db: Session,
    user_id: uuid.UUID,
    data: schema.FeedbackCreate,
) -> Feedback:
    feedback = Feedback(
        category=data.category,
        message=data.message,
        rating=data.rating,
        user_id=user_id,
    )
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback


def get_user_feedbacks(db: Session, user_id: uuid.UUID) -> list[Feedback]:
    return (
        db.query(Feedback)
        .filter(Feedback.user_id == user_id)
        .order_by(Feedback.feedback_id.desc())
        .all()
    )
