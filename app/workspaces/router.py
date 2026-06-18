from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from users.model import User
from users.services import get_current_user
from . import schema, services

router = APIRouter()


@router.post("/", response_model=schema.WorkspaceRead, status_code=status.HTTP_201_CREATED)
def create_workspace(
    data: schema.WorkspaceCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return services.create_workspace(db, current_user.user_id, data)


@router.get("/", response_model=list[schema.WorkspaceRead])
def get_workspaces(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return services.get_user_workspaces(db, current_user.user_id)


@router.get("/{workspace_id}", response_model=schema.WorkspaceRead)
def get_workspace(
    workspace_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return services.get_workspace_or_404(db, workspace_id, current_user.user_id)


@router.patch("/{workspace_id}", response_model=schema.WorkspaceRead)
def update_workspace(
    workspace_id: int,
    data: schema.WorkspaceUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    workspace = services.get_workspace_or_404(db, workspace_id, current_user.user_id)
    return services.update_workspace(db, workspace, data)


@router.delete("/{workspace_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_workspace(
    workspace_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    workspace = services.get_workspace_or_404(db, workspace_id, current_user.user_id)
    services.delete_workspace(db, workspace)
