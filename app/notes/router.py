from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from users.model import User
from users.services import get_current_user
from . import schema, services

router = APIRouter()
workspace_notes_router = APIRouter()


@workspace_notes_router.post(
    "/{workspace_id}/notes",
    response_model=schema.NoteRead,
    status_code=status.HTTP_201_CREATED,
)
def create_note(
    workspace_id: int,
    data: schema.NoteCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return services.create_note(db, workspace_id, current_user.user_id, data)


@workspace_notes_router.get("/{workspace_id}/notes", response_model=list[schema.NoteRead])
def get_workspace_notes(
    workspace_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return services.get_workspace_notes(db, workspace_id, current_user.user_id)


@router.get("/{note_id}", response_model=schema.NoteRead)
def get_note(
    note_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return services.get_note_or_404(db, note_id, current_user.user_id)


@router.patch("/{note_id}", response_model=schema.NoteRead)
def update_note(
    note_id: int,
    data: schema.NoteUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    note = services.get_note_or_404(db, note_id, current_user.user_id)
    return services.update_note(db, note, data)


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(
    note_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    note = services.get_note_or_404(db, note_id, current_user.user_id)
    services.delete_note(db, note)
