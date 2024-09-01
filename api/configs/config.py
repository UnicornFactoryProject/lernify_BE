from decouple import config
from pathlib import Path
from pydantic_settings import BaseSettings

# Use this to build paths inside the project
BASE_DIR = Path(__file__).resolve().parent

class Config():
    """Class to manage the application config environment variables."""

    # Database configurations
    DB_HOST: str = config("DB_HOST")
    DB_PORT: int = config("DB_PORT", cast=int)
    DB_USER: str = config("DB_USER")
    DB_PASSWORD: str = config("DB_PASSWORD")
    DB_NAME: str = config("DB_NAME")
    DB_TYPE: str = config("DB_TYPE")
    DB_URL: str = config("DB_URL")

    # JWT configurations
    ACCESS_TOKEN_EXPIRY: int = config("ACCESS_TOKEN_EXPIRY", cast=int)
    ACCESS_TOKEN_SECRET: str = config("ACCESS_TOKEN_SECRET")
    ACCESS_TOKEN_ALGORITHM: str = config("ACCESS_TOKEN_ALGORITHM")

    # Email configurations
    MAIL_USERNAME: str = config("MAIL_USERNAME")
    MAIL_PASSWORD: str = config("MAIL_PASSWORD")
    MAIL_SERVER: str = config("MAIL_SERVER")
    MAIL_FROM_NAME: str = config("MAIL_FROM_NAME")
    MAIL_FROM: str = config("MAIL_FROM")


config = Config()