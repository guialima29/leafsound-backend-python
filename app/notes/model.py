from sqlalchemy import Boolean, Column, ForeignKey, Integer, JSON, String

from database import Base


class Note(Base):
    __tablename__ = 'notes'

    note_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    content = Column("note_content", JSON, nullable=False)
    note_title = Column(String, nullable=False)
    note_fav = Column(Boolean, default=False, nullable=False)

    workspace_id = Column(
        Integer,
        ForeignKey('workspaces.workspace_id'),
        nullable=False
    )

    @property
    def title(self):
        return self.note_title

    @property
    def is_favorite(self):
        return self.note_fav
