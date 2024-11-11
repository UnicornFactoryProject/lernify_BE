from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.user import User, UserRoleEnum
from app.schemas.user import UserCreate, UserResponse
from app.security import hash_password
from app.dependencies import get_db_session

router = APIRouter()

# Dependency to get the DB session
def get_db(db: Session = Depends(get_db_session)):
    return db

@router.post("/signup", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password before storing it
    hashed_password = hash_password(user.password)
    
    # Create new user instance
    db_user = User(
        full_name=user.full_name,
        email=user.email,
        password=hashed_password,
        role=user.role
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
