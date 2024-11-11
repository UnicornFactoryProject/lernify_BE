from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Database connection string
SQLALCHEMY_DATABASE_URL = f"{settings.DB_TYPE}://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

# Create engine and sessionmaker
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})  # For SQLite, omit `check_same_thread`
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
