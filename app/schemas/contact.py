from pydantic import BaseModel

class ContactBase(BaseModel):
    name: str
    email: str
    message: str

class ContactResponse(ContactBase):
    id: int

    class Config:
        orm_mode = True
