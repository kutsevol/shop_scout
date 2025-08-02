from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "App"}


def test_read_stores():
    response = client.get("/stores/")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Auchan"},
        {"id": 2, "name": "Metro"},
        {"id": 3, "name": "Silpo"},
    ]


def test_read_store():
    response = client.get("/store/1/")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Auchan"}


def test_read_single_store_not_found():
    response = client.get("/store/999999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Store not found"
