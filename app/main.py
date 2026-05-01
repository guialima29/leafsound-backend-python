from fastapi import FastAPI

from users.router import router as user_router
from workspaces.router import router as workspace_router
from notes.router import router as notes_router

from database import Base, engine

from users import model as user_model
from workspaces import model as workspace_model
from notes import model as note_model

Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. Create, read, update and delete users."
    },
    {
        "name": "workspaces",
        "description": "Operations with workspaces. Create, read, update and delete workspaces."
    },
    {
        "name": "notes",
        "description": "Operations with notes. Create, read, update and delete notes."
    }
]

app = FastAPI(openapi_tags=tags_metadata)

app.include_router(
    user_router, prefix="/users", tags=["users"]
)

app.include_router(
    workspace_router, prefix="/workspaces", tags=["workspaces"]
)

app.include_router(
    notes_router, prefix="/notes", tags=["notes"]
)

@app.get("/", tags=["root"])
def read_root():
    return {"Hello": "World"}