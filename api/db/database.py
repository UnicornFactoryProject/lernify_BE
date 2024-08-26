""" Database module to manage database connections.
"""
""" The database module
"""
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from sqlalchemy import create_engine
from api.utils.config import config, BASE_DIR

Base = declarative_base()


DB_HOST = config.DB_HOST
DB_PORT = config.DB_PORT
DB_USER = config.DB_USER
DB_PASSWORD = config.DB_PASSWORD
DB_NAME = config.DB_NAME
DB_TYPE = config.DB_TYPE


def get_db_engine():
    """ Function to get the database engine.
    """

    if DB_TYPE == "sqlite":
        DATABASE_URL = f"sqlite:///{BASE_DIR / 'learnify.db'}"
        return create_engine(
                DATABASE_URL, connect_args={"check_same_thread": False}
            )
    elif DB_TYPE == "postgresql":
        DATABASE_URL = (
            f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )
        return create_engine(DATABASE_URL)
    else:
        raise ValueError(f"Unsupported DB_TYPE: {DB_TYPE}")



engine = get_db_engine()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db_session = scoped_session(SessionLocal)

def create_database():
    """Create all tables in the database as defined in the Base metadata.
    This function should be called to initialize the database schema.
    """
    return Base.metadata.create_all(bind=engine)


def get_db():
    """Provide a database session.
    
    This function is a generator that yields a database session and ensures
    it is closed after use.
    """
    db = db_session()
    try:
        yield db
    finally:
        db.close()