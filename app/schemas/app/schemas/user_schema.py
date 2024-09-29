from pydantic import BaseModel, EmailStr

class UserSignUp(BaseModel):
    full_name: str
    email: EmailStr
    password: str