from fastapi import Depends, APIRouter, Request, status, Query, HTTPException
from sqlalchemy.orm import Session
# from api.v1.services.user import UserService


user_router = APIRouter(prefix="/users", tags=["Users"])

@user_router.get('', status_code=status.HTTP_200_OK)
async def get_users(db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.get_all_users()

