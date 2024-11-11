import os  # Import os module
from pydantic import BaseSettings
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL")
    secret_key: str = os.getenv("SECRET_KEY")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    algorithm: str = os.getenv("ALGORITHM")
    # Add other variables similarly

# Instantiate settings
settings = Settings()
