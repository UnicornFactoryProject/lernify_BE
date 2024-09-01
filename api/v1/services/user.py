from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from api.v1.models import User
from typing import List
from api.db.database import get_db
from fastapi import HTTPException
from api.utils.auth_utils import hash_password, verify_password
from api.v1.schemas import user
import secrets

class UserService():
    """User service
    """
    def __init__(self, db: Session):
        self.db = db

    def get_all_users(self) -> List[User]:
        return self.db.query(User).all()
    
    def create_user(self, db: Session, schema: user.CreateUserSchema) -> User:
        """Create a new user
        """
        is_user_exist = db.query(User).filter(User.email == schema.email).first()
        if is_user_exist:
            if is_user_exist.is_deleted:
                raise HTTPException(status_code=400, detail="User with this credentials is deactivated, contact support")
            raise HTTPException(status_code=400, detail="User already exists")

        schema.password = hash_password(schema.password)

        new_user = User(**schema.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
    def login_user(self, db: Session, email: str, password: str):
        """ Login a user
        """

        user = db.query(User).filter(User.email == email).first()

        if not user:
            raise HTTPException(status_code=400, detail="Invalid user credentials")

        if not verify_password(password, user.password):
            raise HTTPException(status_code=400, detail="Invalid user credentials")

        return user
    
    def password_reset_request(self, db: Session, email: str):
        """Password reset request
        """
        user = db.query(User).filter(User.email == email).first()

        if not user:
            raise HTTPException(status_code=404, detail="User with this email does not exist")
        
        token = secrets.token_urlsafe(20)
        expiry = datetime.now() + timedelta(hours=1)
        user.password_reset_token = token
        user.password_reset_token_expiry = expiry
        db.commit()
        return user
    
    def reset_password(self, db: Session, schema = user.PasswordResetSchema):
        """ Validate password reset token and reset password
        """
        user = db.query(User).filter(User.password_reset_token == schema.token).first()
        if not user:
            raise HTTPException(status_code=404, detail="Invalid token")
        
        expiry_datetime = datetime.strptime(user.password_reset_token_expiry, "%Y-%m-%d %H:%M:%S.%f")
        if expiry_datetime < datetime.now():
            raise HTTPException(status_code=400, detail="Token expired")
        
        user.password = hash_password(schema.new_password)
        user.password_reset_token = None
        user.password_reset_token_expiry = None
        db.commit()
        return user