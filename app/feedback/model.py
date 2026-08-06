import enum
import uuid

from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, String, func
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class FeedbackCategory(str, enum.Enum):
    BUG = "bug"
    IDEA = "idea"
    LIKE = "like"
    DISLIKE = "dislike"
    OTHER = "other"


class FeedbackStatus(str, enum.Enum):
    NEW = "new"
    REVIEWED = "reviewed"
    PLANNED = "planned"
    CLOSED = "closed"


class Feedback(Base):
    __tablename__ = 'feedbacks'

    feedback_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    category = Column(
        SqlEnum(FeedbackCategory, name="feedback_category", values_callable=lambda enum_cls: [e.value for e in enum_cls]),
        nullable=False,
    )
    message = Column(String(2000), nullable=False)
    rating = Column(SmallInteger, nullable=True)
    status = Column(
        SqlEnum(FeedbackStatus, name="feedback_status", values_callable=lambda enum_cls: [e.value for e in enum_cls]),
        nullable=False,
        default=FeedbackStatus.NEW,
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey('users.user_id'),
        nullable=False,
    )
