import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: uuid.UUID
    user_name: str
    user_email: EmailStr
    avatar_url: str | None = None
    created_at: datetime
    updated_at: datetime


class UserUpdate(BaseModel):
    user_name: str = Field(min_length=1, max_length=120)


class GoogleLoginRequest(BaseModel):
    id_token: str = Field(min_length=1)


class DevLoginRequest(BaseModel):
    user_name: str = Field(min_length=1, max_length=120)
    user_email: EmailStr
    avatar_url: str | None = None


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserRead
