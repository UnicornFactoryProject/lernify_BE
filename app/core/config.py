import os
from pydantic import BaseSettings
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Settings(BaseSettings):
    # Database connection settings
    database_url: str = os.getenv("DATABASE_URL")
    secret_key: str = os.getenv("SECRET_KEY")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    algorithm: str = os.getenv("ALGORITHM")

    # PostgreSQL (or SQLite) settings
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: int = int(os.getenv("DB_PORT"))
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_TYPE: str = os.getenv("DB_TYPE", "postgresql")  # Default to 'postgresql'

    class Config:
        env_file = ".env"

# Instantiate settings
settings = Settings()
