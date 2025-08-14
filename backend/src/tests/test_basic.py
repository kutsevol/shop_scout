from unittest.mock import AsyncMock, patch

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from api.routers import countries, index, shops
from services.fetch_stores import fetch_stores
from services.search_products import search_products


@pytest.fixture
def app() -> FastAPI:
    app = FastAPI()
    app.include_router(index.router)
    app.include_router(shops.router)
    app.include_router(countries.router)
    return app


@pytest.fixture
def async_client(app: FastAPI):
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


@pytest.mark.asyncio
async def test_read_index(async_client):
    response = await async_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "App"}


@pytest.mark.asyncio
async def test_get_countries(async_client):
    response = await async_client.get("/countries/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_shops(async_client):
    response = await async_client.get("/shops/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "id" in data[0]
        assert "name" in data[0]


MOCKED_RESPONSE = [{"id": "1", "name": "Shop One"}, {"id": "2", "name": "Shop Two"}]


@pytest.mark.asyncio
async def test_get_shops_success(async_client):
    with patch("api.routers.shops.fetch_stores", new=AsyncMock(return_value=MOCKED_RESPONSE)):
        response = await async_client.get("/shops/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert data == MOCKED_RESPONSE


@pytest.mark.asyncio
async def test_get_shop_not_found(async_client):
    response = await async_client.get("/shops/999999/")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_fetch_stores(async_client):
    stores = await fetch_stores()
    assert isinstance(stores, list)
    if stores:
        assert "id" in stores[0]
        assert "name" in stores[0]


@pytest.mark.asyncio
async def test_search_products(async_client):
    stores = await fetch_stores()
    if not stores:
        pytest.skip("No stores available to test product search")

    store_id = stores[0]["id"]
    products = await search_products(store_id=store_id, query="milk")
    assert isinstance(products, list)
    for product in products:
        assert "store_id" in product
        assert product["store_id"] == store_id
