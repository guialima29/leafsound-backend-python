from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from variables import database_connection

DATABASE_URL = database_connection

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()