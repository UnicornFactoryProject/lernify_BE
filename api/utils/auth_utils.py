from passlib.context import CryptContext
import datetime
from api.utils.config import config
from jose import jwt, JWTError
from fastapi import HTTPException

# Initialize the CryptContext with your hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Function to hash a password
    """
    hashed_password = pwd_context.hash(password)
    return hashed_password

def verify_password(password: str, hash: str) -> bool:
    """verify a hashed password
    """
    return pwd_context.verify(secret=password, hash=hash)

def generate_access_token(user_id: str ):
    """ Method to generate access token
    """
    expiry_period = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=config.ACCESS_TOKEN_EXPIRY)
    data = {"user_id": user_id, "exp": expiry_period, "role": "user"}
    encoded_jwt = jwt.encode(data, config.ACCESS_TOKEN_SECRET, algorithm=config.ACCESS_TOKEN_ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str):
    """ Verify jwt access token
    """
    try:
        decode = jwt.decode(token, config.ACCESS_TOKEN_SECRET, algorithms=[config.ACCESS_TOKEN_ALGORITHM])
        user_id = decode.get("user_id")
        role = decode.get("role")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Unauthorized")    
    except JWTError:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user_id


