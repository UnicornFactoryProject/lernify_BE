from fastapi import Depends, APIRouter, Request, status, Response
from sqlalchemy.orm import Session
from api.v1.models.user import User
from api.db.database import get_db
from api.v1.services.user import UserService
from api.v1.schemas.user import CreateUserSchema, LoginUserSchema
from fastapi.encoders import jsonable_encoder
from api.utils.json_response import auth_response
from api.utils.auth_utils import generate_access_token


auth_router = APIRouter(prefix="/auth", tags=["Authentication"])

@auth_router.post('/register', status_code=status.HTTP_201_CREATED)
async def reister_user(request: Request, response: Response, user_schema: CreateUserSchema, db: Session = Depends(get_db)):
    user_service = UserService(db)
    new_user = user_service.create_user(db, user_schema)

    ## Generate token
    token = generate_access_token(new_user.id)

    # Background task to send email
    ##TODO

    return auth_response(
        status_code=201,
        message='Registration successful',
        access_token=token,
        data={
            'user': jsonable_encoder(
                new_user,
                exclude=['password', 'is_deleted', 'is_verified']
            ),
        }
    )

@auth_router.post('/login', status_code=status.HTTP_200_OK)
async def login_user(request: Request, response: Response, login_schema: LoginUserSchema, db: Session = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.login_user(db, login_schema.email, login_schema.password)

    ## Generate token
    token = generate_access_token(user.id)

    return auth_response(
        status_code=200,
        message='Login successful',
        access_token=token,
        data={
            'user': jsonable_encoder(
                user,
                exclude=['password', 'is_deleted', 'is_verified']
            ),
        }
    )