from decouple import config
from pathlib import Path
from pydantic_settings import BaseSettings

# Use this to build paths inside the project
BASE_DIR = Path(__file__).resolve().parent

class Config():
    """Class to manage the application config environment variables."""
    print("Hello")


    # Database configurations
    DB_HOST: str = config("DB_HOST")
    DB_PORT: int = config("DB_PORT", cast=int)
    DB_USER: str = config("DB_USER")
    DB_PASSWORD: str = config("DB_PASSWORD")
    DB_NAME: str = config("DB_NAME")
    DB_TYPE: str = config("DB_TYPE")
    DB_URL: str = config("DB_URL")
    ACCESS_TOKEN_EXPIRY: int = config("ACCESS_TOKEN_EXPIRY", cast=int)
    ACCESS_TOKEN_SECRET: str = config("ACCESS_TOKEN_SECRET")
    ACCESS_TOKEN_ALGORITHM: str = config("ACCESS_TOKEN_ALGORITHM")


config = Config()