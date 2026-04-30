from pydantic import BaseModel
from typing import Any

class NoteCreation(BaseModel):
    title: str
    content: dict[str, Any]
    note_fav: bool
    workspace_id: int