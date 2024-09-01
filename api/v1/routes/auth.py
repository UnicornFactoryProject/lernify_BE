from fastapi import Depends, APIRouter, Request, status, Response, BackgroundTasks
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from api.v1.models.user import User
from api.db.database import get_db
from api.v1.services.user import UserService
from api.v1.schemas.user import CreateUserSchema, LoginUserSchema, ForgotPasswordSchema, PasswordResetSchema
from fastapi.encoders import jsonable_encoder
from api.utils.json_response import auth_response
from api.utils.auth_utils import generate_access_token
from api.utils.email_utils import send_email
from api.configs.config import config


auth_router = APIRouter(prefix="/auth", tags=["Authentication"])

@auth_router.post('/register', status_code=status.HTTP_201_CREATED)
async def reister_user(background_task: BackgroundTasks, request: Request, response: Response, user_schema: CreateUserSchema, db: Session = Depends(get_db)):
    user_service = UserService(db)
    new_user = user_service.create_user(db, user_schema)

    ## Generate token
    token = generate_access_token(new_user.id)

    # Background task to send email
    background_task.add_task(
        send_email,
        subject="Welcome to Learnify e-Learning",
        recipients=[new_user.email],
        template_name="welcome_template.html",
        context={"first_name": new_user.first_name.capitalize()},
    )

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


@auth_router.post('/forgot-password', status_code=status.HTTP_200_OK)
async def forgot_password(request: Request, response: Response, background_task: BackgroundTasks, schema: ForgotPasswordSchema, db: Session = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.password_reset_request(db, schema.email)

    reset_link = f"{config.FRONTEND_BASE_URL}/reset-password?token={user.password_reset_token}"

    # # Background task to send email
    # background_task.add_task(
    #     send_email,
    #     subject="Welcome to Learnify e-Learning",
    #     recipients=[user.email],
    #     template_name="password_reset_template.html",
    #     context={"reset_link": reset_link, "first_name": user.first_name.capitalize()},
    # )

    return JSONResponse(
        status_code=200,
        content={
            "status": 200,
            "message": "Password reset link sent to your email",
        }
    )

@auth_router.post('/reset-password', status_code=status.HTTP_200_OK)
async def reset_password(request: Request, response: Response, schema: PasswordResetSchema, db: Session = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.reset_password(db, schema)

    return JSONResponse(
        status_code=200,
        content={
            "status": 200,
            "message": "Password reset successful",
        }
    )