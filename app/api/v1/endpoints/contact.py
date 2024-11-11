from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.contact import Contact
from app.schemas.contact import ContactBase, ContactResponse
from app.dependencies import get_db_session

router = APIRouter()

# Dependency to get the DB session
def get_db(db: Session = Depends(get_db_session)):
    return db

@router.post("/", response_model=ContactResponse)
def create_contact(contact: ContactBase, db: Session = Depends(get_db)):
    # Save the contact submission to the database
    db_contact = Contact(name=contact.name, email=contact.email, message=contact.message)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact
