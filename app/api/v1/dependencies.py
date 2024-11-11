from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db 
from app.services import auth_service
from app.models import User

# Dependency to get the current database session
def get_db_session(db: Session = Depends(get_db)):
    return db

# Dependency to extract and verify the JWT token
def get_current_user(token: str = Depends(auth_service.get_token)):
    user = auth_service.verify_token(token)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user

# Dependency for checking if a user exists
def user_exists(user_id: int, db: Session = Depends(get_db_session)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
