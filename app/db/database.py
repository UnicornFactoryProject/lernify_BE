from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db  
from app.models.user import User  
from app.schemas.user import UserSignUp 
from app.crud.user import create_user  

router = APIRouter()

@router.post("/signup/")
def sign_up(user: UserSignUp, db: Session = Depends(get_db)):
    """Sign up a new user."""
    
    
    new_user = create_user(db, user)
    
    if not new_user:
        raise HTTPException(status_code=400, detail="Email already used")
    
    
    return {
        "message": "Successfully created uLearnux account",
        "user": {
            "id": new_user.id,
            "full_name": new_user.full_name,
            "email": new_user.email
        }
    }
