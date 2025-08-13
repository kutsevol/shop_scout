from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "App"}


def test_read_shops():
    response = client.get("/shops/")
    assert response.status_code == 200


def test_read_single_shop_not_found():
    response = client.get("/shop/999999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Not Found"
