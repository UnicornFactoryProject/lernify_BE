import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.session import Base, get_db
from app.models.user import User
from app.core.security import get_password_hash

# Set up a test database (use SQLite in memory for simplicity)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency to use the test database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create the test database and tables
Base.metadata.create_all(bind=engine)

# Set up a test client for the app
client = TestClient(app)

@pytest.fixture(scope="module")
def test_user():
    db = TestingSessionLocal()
    # Create a test user in the database
    hashed_password = get_password_hash("testpassword")
    user = User(email="testuser@example.com", hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return {"email": "testuser@example.com", "password": "testpassword"}

def test_sign_in_success(test_user):
    # Successful sign-in with correct credentials
    response = client.post("/api/v1/auth/signin", json={"email": test_user["email"], "password": test_user["password"]})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_sign_in_invalid_email():
    # Attempt to sign in with an invalid email
    response = client.post("/api/v1/auth/signin", json={"email": "wrongemail@example.com", "password": "testpassword"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password"

def test_sign_in_invalid_password(test_user):
    # Attempt to sign in with an incorrect password
    response = client.post("/api/v1/auth/signin", json={"email": test_user["email"], "password": "wrongpassword"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password"
