from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from passlib.context import CryptContext
import os

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Database URL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5432/LearnifyDB"

# Initialize FastAPI app
app = FastAPI()

# SQLAlchemy setup
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Password hashing function
def hash_password(password: str):
    return pwd_context.hash(password)

# Database model for User
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

# Create the database tables (if they don't exist)
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schema for user input validation
class UserSignUp(BaseModel):
    full_name: str
    email: EmailStr
    password: str

# Sign-up route
@app.post("/signup/")
def sign_up(user: UserSignUp, db: Session = Depends(get_db)):
    # Check if user already exists
    user_exists = db.query(User).filter(User.email == user.email).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Email already used")
    
    # Hash the password
    hashed_password = hash_password(user.password)
    
    # Create new user
    new_user = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password
    )
    
    # Save new user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "Successfully created uLearnux account", "user": new_user}