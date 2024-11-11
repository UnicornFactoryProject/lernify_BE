from pydantic import BaseModel, EmailStr, validator
from app.models.user import UserRoleEnum

class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    role: UserRoleEnum

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str

    @validator("password")
    def validate_password(cls, v):
        if not any(char.isupper() for char in v):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not any(char.isdigit() for char in v):
            raise ValueError("Password must contain at least one digit.")
        return v

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
