from fastapi import FastAPI
from app.api.v1 import user, auth, contact
from app.db.init_db import init_db  # Import the init_db function

# Initialize the FastAPI application
app = FastAPI()

# Initialize the database (creates tables if not already present)
init_db()

# Include version 1 routes
app.include_router(user.router, prefix="/api/v1/users", tags=["users"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(contact.router, prefix="/api/v1/contact", tags=["contact"])

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Learnify API!"}
