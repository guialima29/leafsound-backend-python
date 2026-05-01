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


def get_notes(db: Session, workspace_id: int):
    return db.query(Note).filter(Note.workspace_id == workspace_id).all()

def get_single_note(db: Session, note_id: int):
    return db.query(Note).filter(Note.note_id == note_id).first()

def delete_note(db: Session, note_id: int):
    note = db.query(Note).filter(Note.note_id == note_id).first()
    if note:
        db.delete(note)
        db.commit()
        return True
    return False