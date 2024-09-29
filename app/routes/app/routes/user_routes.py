from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserSignUp
from app.crud.user_crud import create_user
from app.database.database import get_db

router = APIRouter()

@router.post("/signup/")
def sign_up(user: UserSignUp, db: Session = Depends(get_db)):
    """Sign up a new user."""
    return create_user(db, user)