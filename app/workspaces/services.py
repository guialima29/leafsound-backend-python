import uuid

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from . import schema
from .model import Workspace

MAX_WORKSPACES_PER_USER = 5


def count_user_workspaces(db: Session, user_id: uuid.UUID) -> int:
    return db.query(Workspace).filter(Workspace.user_id == user_id).count()


def create_workspace(
    db: Session,
    user_id: uuid.UUID,
    data: schema.WorkspaceCreate,
) -> Workspace:
    if count_user_workspaces(db, user_id) >= MAX_WORKSPACES_PER_USER:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Workspace limit reached. Each user can have up to 5 workspaces.",
        )

    workspace = Workspace(
        workspace_name=data.workspace_name,
        user_id=user_id,
    )
    db.add(workspace)
    db.commit()
    db.refresh(workspace)
    return workspace


def get_user_workspaces(db: Session, user_id: uuid.UUID) -> list[Workspace]:
    return (
        db.query(Workspace)
        .filter(Workspace.user_id == user_id)
        .order_by(Workspace.workspace_id.desc())
        .all()
    )


def get_workspace_or_404(
    db: Session,
    workspace_id: int,
    user_id: uuid.UUID,
) -> Workspace:
    workspace = (
        db.query(Workspace)
        .filter(
            Workspace.workspace_id == workspace_id,
            Workspace.user_id == user_id,
        )
        .first()
    )

    if not workspace:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workspace not found",
        )

    return workspace


def update_workspace(
    db: Session,
    workspace: Workspace,
    data: schema.WorkspaceUpdate,
) -> Workspace:
    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(workspace, field, value)

    db.commit()
    db.refresh(workspace)
    return workspace


def delete_workspace(db: Session, workspace: Workspace) -> None:
    db.delete(workspace)
    db.commit()
