from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/api/v1/signup", json={
        "full_name": "John Doe",
        "email": "john.doe@example.com",
        "password": "Password123",
        "role": "student"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "john.doe@example.com"
    assert response.json()["role"] == "student"
