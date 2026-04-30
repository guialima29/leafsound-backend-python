from sqlalchemy.orm import Session
from .model import Note
from . import schema

def create_note(db: Session, note: schema.NoteCreation):
    db_note = Note(
        note_title=note.title,
        note_content=note.content,
        note_fav=note.note_fav,
        workspace_id=note.workspace_id
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note