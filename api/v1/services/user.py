from sqlalchemy.orm import Session
from api.v1.models import User
from typing import List
from api.db.database import get_db

class UserService():
    """User service
    """
    def __init__(self, db: Session):
        self.db = db

    def get_all_users(self) -> List[User]:
        return self.db.query(User).all()
    