import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from .model import FeedbackCategory, FeedbackStatus


class FeedbackCreate(BaseModel):
    category: FeedbackCategory
    message: str = Field(min_length=1, max_length=2000)
    rating: int | None = Field(default=None, ge=1, le=5)


class FeedbackRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    feedback_id: int
    user_id: uuid.UUID
    category: FeedbackCategory
    message: str
    rating: int | None
    status: FeedbackStatus
    created_at: datetime
