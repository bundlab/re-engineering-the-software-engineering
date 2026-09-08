from fastapi.testclient import TestClient
from app.main import app, db

client = TestClient(app)

def setup_function():
    db.clear()

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_and_get_item():
    payload = {"id": 101, "name": "Test Gadget", "price": 29.99}
    
    # Create item
    res_post = client.post("/items/", json=payload)
    assert res_post.status_code == 201
    
    # Fetch item
    res_get = client.get("/items/101")
    assert res_get.status_code == 200
    assert res_get.json()["name"] == "Test Gadget"

def test_get_nonexistent_item():
    response = client.get("/items/999")
    assert response.status_code == 404
