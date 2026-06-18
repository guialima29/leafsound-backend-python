import uuid

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from workspaces.services import get_workspace_or_404
from . import schema
from .model import Note


def create_note(
    db: Session,
    workspace_id: int,
    user_id: uuid.UUID,
    data: schema.NoteCreate,
) -> Note:
    get_workspace_or_404(db, workspace_id, user_id)

    note = Note(
        content=data.content,
        workspace_id=workspace_id,
        note_title=data.title,
        note_fav=data.is_favorite,
    )
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


def get_workspace_notes(
    db: Session,
    workspace_id: int,
    user_id: uuid.UUID,
) -> list[Note]:
    get_workspace_or_404(db, workspace_id, user_id)

    return (
        db.query(Note)
        .filter(Note.workspace_id == workspace_id)
        .order_by(Note.note_id.desc())
        .all()
    )


def get_note_or_404(
    db: Session,
    note_id: int,
    user_id: uuid.UUID,
) -> Note:
    note = db.query(Note).filter(Note.note_id == note_id).first()

    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found",
        )

    get_workspace_or_404(db, note.workspace_id, user_id)
    return note


def update_note(
    db: Session,
    note: Note,
    data: schema.NoteUpdate,
) -> Note:
    update_data = data.model_dump(exclude_unset=True)

    if "title" in update_data:
        note.note_title = update_data["title"]

    if "is_favorite" in update_data:
        note.note_fav = update_data["is_favorite"]

    if "content" in update_data:
        note.content = update_data["content"]

    db.commit()
    db.refresh(note)
    return note


def delete_note(db: Session, note: Note) -> None:
    db.delete(note)
    db.commit()
