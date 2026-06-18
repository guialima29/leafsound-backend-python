from fastapi import FastAPI

from users.router import auth_router, router as user_router
from workspaces.router import router as workspace_router
from notes.router import router as notes_router, workspace_notes_router

from database import Base, engine

from users import model as user_model
from workspaces import model as workspace_model
from notes import model as note_model

Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "root",
        "description": "Health check and root endpoints."
    },
    {
        "name": "auth",
        "description": "Authentication endpoints. Use dev login for local tests and Google login for the real app."
    },
    {
        "name": "users",
        "description": "Operations with the authenticated user."
    },
    {
        "name": "workspaces",
        "description": "Create, read, update and delete workspaces for the authenticated user."
    },
    {
        "name": "notes",
        "description": "Create, read, update and delete notes inside user workspaces."
    }
]

app = FastAPI(
    title="LeafSound Backend",
    description="API for users, authentication, workspaces, notes and feedback in LeafSound.",
    version="0.1.0",
    openapi_tags=tags_metadata,
)

app.include_router(
    user_router, prefix="/users", tags=["users"]
)

app.include_router(
    auth_router, prefix="/auth", tags=["auth"]
)

app.include_router(
    workspace_router, prefix="/workspaces", tags=["workspaces"]
)

app.include_router(
    workspace_notes_router, prefix="/workspaces", tags=["notes"]
)

app.include_router(
    notes_router, prefix="/notes", tags=["notes"]
)

@app.get("/", tags=["root"])
def read_root():
    return {"Hello": "World"}
