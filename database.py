from sqlalchemy import create_engine

DATABASE_URL = "postgres://user:password@localhost:5432/db"

engine = create_engine(DATABASE_URL)