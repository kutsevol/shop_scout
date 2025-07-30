from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "App"}


def test_read_stores():
    response = client.get("/stores")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "Auchan"}, {"id": 2, "name": "Metro"}]


def test_read_store():
    response = client.get("/store/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Auchan"}
