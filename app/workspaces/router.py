from fastapi import APIRouter

router = APIRouter()

@router.post("/{user_id}")
def createWorkspace(user_id: int):
    return {"message":f"{user_id}'s workspace created"}

@router.get("/{user_id}")
def getWorkspaces(user_id: int):
    return {"message": f"user {user_id} workspaces:"}

@router.delete("/{workspace_id}")
def deleteWorkspace(workspace_id: int):
    return {"message": f"{workspace_id} deleted!"}