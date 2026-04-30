from fastapi import APIRouter

router = APIRouter()

@router.post("/register/{email}")
def registerUser(email: str):
    return {"message": f"user {email} registered!"}

@router.get("/login")
def loginUser():
    return {"message": "login executed"}
