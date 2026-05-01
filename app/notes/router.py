from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from . import schema, services

router = APIRouter()

@router.post("/")
def createNote(data: schema.NoteCreation, db: Session = Depends(get_db)):
    result = services.create_note(db, data)

    return {
        "message": "Note created successfully!",
        "note": {
            "note_id": result.note_id,
            "note_title": result.note_title,
            "note_fav": result.note_fav,
            "note_content": result.note_content
        }
    }


# TODO: implement these functions below
@router.get("/{workspace_id}")
def getNotes(workspace_id):
    result = services.get_notes(workspace_id)
    return result

@router.get("/note/{id}")
def getSingleNote(id: int):
    result = services.get_single_note(id)
    if result:        
        return {
            "note_id": result.note_id,
            "note_title": result.note_title,
            "note_fav": result.note_fav,
            "note_content": result.note_content
        }
    return { "title": f"Note {id}", "content": "content"}

@router.delete("/{id}")
def deleteNote(id: int):
    result = services.delete_note(id)
    if result:
        return {"message": f"Note {id} deleted!"}
    return {"message": f"Note {id} not found!"}