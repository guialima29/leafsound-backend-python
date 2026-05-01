from sqlalchemy import Column, Integer, String, Boolean, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Note(Base):
    __tablename__ = 'notes'

    note_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    note_title = Column(String, unique=True)
    note_fav = Column(Boolean, nullable=False)
    note_content = Column(JSON, nullable=False)

    workspace_id = Column(
        Integer, 
        ForeignKey('workspaces.workspace_id'), 
        nullable=False
        )