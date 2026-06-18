from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    is_favorite: bool = False
    content: dict[str, Any]


class NoteUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    is_favorite: bool | None = None
    content: dict[str, Any] | None = None


class NoteRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    note_id: int
    workspace_id: int
    title: str
    is_favorite: bool
    content: dict[str, Any]
