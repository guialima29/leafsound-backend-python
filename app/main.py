from fastapi import FastAPI

from users.router import router as user_router
from workspaces.router import router as workspace_router
from notes.router import router as notes_router

app = FastAPI()


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