from sqlalchemy.orm import Session
from api.v1.models import User
from typing import List
from api.db.database import get_db
from fastapi import HTTPException
from api.utils.auth_utils import hash_password
from api.v1.schemas import user

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