from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Workspace(Base):
    __tablename__ = 'workspaces'

    workspace_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    workspace_name = Column(String, unique=True)

    user_id = Column(
        Integer, 
        ForeignKey('users.user_id'), 
        nullable=False
        ) 