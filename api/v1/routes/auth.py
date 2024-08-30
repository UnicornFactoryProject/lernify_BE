from fastapi import Depends, APIRouter, Request, status, Response
from sqlalchemy.orm import Session
from api.v1.models.user import User
from api.db.database import get_db
from api.v1.services.user import UserService
from api.v1.schemas.user import CreateUserSchema


auth_router = APIRouter(prefix="/auth", tags=["Authentication"])

@auth_router.post('/register', status_code=status.HTTP_201_CREATED)
async def reister_user(request: Request, response: Response, user_schema: CreateUserSchema, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.create_user(db, user_schema)