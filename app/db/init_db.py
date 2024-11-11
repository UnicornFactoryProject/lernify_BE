from app.db import session, base
from app.models import User, Contact  # Import all models to ensure they are registered

def init_db():
    # Create all tables in the database
    base.Base.metadata.create_all(bind=session.engine)
