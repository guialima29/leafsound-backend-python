from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class Workspace(Base):
    __tablename__ = 'workspaces'

    workspace_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    workspace_name = Column(String, nullable=False)

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey('users.user_id'),
        nullable=False
    )
