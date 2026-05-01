from sqlalchemy import Column, Integer, String, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(UUID, primary_key=True, unique=True, index=True)
    user_name = Column(String, unique=True)
    user_email = Column(String, unique=False)