from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user_model import User
from app.schemas.user_schema import UserSignUp
from app.utils.password import hash_password

def create_user(db: Session, user: UserSignUp):
    """Create a new user."""
    
    user_exists = db.query(User).filter(User.email == user.email).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Email already used")

    
    hashed_password = hash_password(user.password)

    
    new_user = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password
    )

    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "Successfully created Learnify account",
        "user": {
            "id": new_user.id,
            "full_name": new_user.full_name,
            "email": new_user.email
        }
    }
