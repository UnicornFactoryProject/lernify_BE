""" User data model
"""

from sqlalchemy import Column, String, text, Boolean, Integer
from sqlalchemy.orm import relationship
from app.db.database import Base


class ExamUser(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)

    email = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password = Column(String, nullable=True)
    avatar_url = Column(String, nullable=True)
    password_reset_token = Column(String, nullable=True)
    password_reset_token_expiry = Column(String, nullable=True)
    google_id = Column(String, nullable=True)
    is_deleted = Column(Boolean, server_default=text("false"))
    is_verified = Column(Boolean, server_default=text("false"))