from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_create_person():
    response = client.post("/api", json={"name": "bolaji"})
    assert response.status_code == 201

def test_get_person():
    response = client.get("/api/bolaji")
    assert response.status_code == 200

def test_update_person():
    response = client.put("/api/bolaji", json={"name": "jenny"})
    assert response.status_code == 200

def test_delete_person():
    response = client.delete("/api/jenny")
    assert response.status_code == 204
