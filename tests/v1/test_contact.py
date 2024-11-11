from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_contact():
    # Submit a contact form
    response = client.post("/api/v1/contact/", json={"name": "John Doe", "email": "john.doe@example.com", "message": "Hello, I need assistance."})
    
    # Check if the response is valid
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"
    assert response.json()["message"] == "Hello, I need assistance."
