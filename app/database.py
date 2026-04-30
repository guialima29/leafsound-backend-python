from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.notes.model import Base

DATABASE_URL = "postgresql://postgres:postgres@localhost/leafsound"

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
    )


SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()