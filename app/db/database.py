""" 
Database module to manage database connections.

"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.configs import config

DB_HOST = config.DB_HOST
DB_PORT = config.DB_PORT
DB_USER = config.DB_USER
DB_PASSWORD = config.DB_PASSWORD
DB_NAME = config.DB_NAME


DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL,
                       pool_size=10, # max connections in the pool
                       max_overflow=20, # extra connectionsif the pool is full
                       pool_timeout=30, # timeout to acquire connection from pool
                       pool_recycle=1800 # seconds to recycle the connection
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()