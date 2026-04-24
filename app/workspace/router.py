from fastapi import APIRouter

router = APIRouter()

@router.post("/{user_id}")
def createWorkspace():
    return {"message":"{user_id}'s workspace created"}

@router.get("/{user_id}")
def getWorkspaces(user_id: int):
    return {"message": "user {user_id} workspaces:"}

@router.delete("/{workspace_id}")
def deleteWorkspace(workspace_id: int):
    return {"message": "{workspace_id} deleted!"}