from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from typing import Annotated
from app.configs import config
from app.db.database import get_db
from app.crud import user_crud # define a user crud i.e get user by email
from jose import jwt, JWTError
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from google.oauth2 import id_token
from google.auth.transport import requests


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Initialize the CryptContext with your hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)



def generate_access_token(data:dict) -> str:
    to_encode = data.copy()
    expiry_time = datetime.now(timezone.utc) + timedelta(minutes=config.ACCESS_TOKEN_EXPIRY)
    to_encode.update({"exp":expiry_time})
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt



def verify_access_token(token:Annotated[str, Depends(oauth2_scheme)], session=Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                          detail="Could not validate credentials", 
                                          headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        email:str = payload.get("sub")
        if not email:
            raise credentials_exception   
    except JWTError:
        raise credentials_exception
    user = user_crud.get_user_by_email(session, email=email)
    if user is None:
        raise credentials_exception
    return user


def authenticate_user(session: Session, email:str, password:str):
    user = user_crud.get_user_by_email(session, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user




def verify_google_token(token: str):
    """ Verify google id token
    """
    try:
        id_info = id_token.verify_oauth2_token(token, requests.Request(), config.GOOGLE_CLIENT_ID) # not gotten google client id yet
        # Optionally, verify that the token was issued for the correct audience

        if id_info["aud"] != config.GOOGLE_CLIENT_ID:
            raise ValueError('Invalid audience')
        return id_info   
    except ValueError:
        return None
