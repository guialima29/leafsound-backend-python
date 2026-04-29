from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def createNote():
    return { "message": "Note created!"}

@router.get("/{workspace_id}")
def getNotes(workspace_id):
    return { "message": f"listing {workspace_id} notes..."}

@router.get("/note/{id}")
def getSingleNote(id: int):
    return { "title": f"Note {id}", "content": "content"}

@router.delete("/{id}")
def deleteNote(id: int):
    return {"message": f"Note {id} deleted!"}