from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_add_and_list_patient():
    response = client.post("/patients", headers={"api_key":"secret123"}, params={"name":"Alice"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Alice"

    response = client.get("/patients")
    assert response.status_code == 200
    assert len(response.json()) == 1
