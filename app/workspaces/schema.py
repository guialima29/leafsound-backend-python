import uuid

from pydantic import BaseModel, ConfigDict, Field


class WorkspaceCreate(BaseModel):
    workspace_name: str = Field(min_length=1, max_length=120)


class WorkspaceUpdate(BaseModel):
    workspace_name: str = Field(min_length=1, max_length=120)


class WorkspaceRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    workspace_id: int
    workspace_name: str
    user_id: uuid.UUID
