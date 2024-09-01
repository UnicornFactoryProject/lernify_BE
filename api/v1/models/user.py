""" User data model
"""

from sqlalchemy import Column, String, text, Boolean
from sqlalchemy.orm import relationship
from api.v1.models.base_model import BaseTableModel


class User(BaseTableModel):
    __tablename__ = "users"

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