from contextlib import asynccontextmanager

import httpx
import pytest
from httpx import MockTransport, Request, Response

import pipeline.extractor.extractor as extractor
from dto.category import Category
from dto.product import Product
from pipeline.extractor.client import DEFAULT_HEADERS


def make_mock_transport(handler):
    return MockTransport(handler)


@pytest.mark.asyncio
async def test_create_http_client_basic(monkeypatch):
    created_args = {}

    class DummyClient(httpx.AsyncClient):
        def __init__(self, *args, **kwargs):
            created_args.update(kwargs)
            super().__init__(*args, **kwargs)

    monkeypatch.setattr("httpx.AsyncClient", DummyClient)

    async with extractor.create_http_client() as client:
        assert isinstance(client, httpx.AsyncClient)
        assert created_args["headers"] == DEFAULT_HEADERS
        assert created_args["timeout"] == 60


@pytest.mark.asyncio
async def test_create_http_client_with_request(monkeypatch):
    def mock_handler(request: Request) -> Response:
        assert request.url.path == "/test"
        return Response(200, json={"ok": True})

    transport = MockTransport(mock_handler)

    monkeypatch.setattr(
        extractor,
        "create_http_client",
        lambda: httpx.AsyncClient(headers=DEFAULT_HEADERS, timeout=60, transport=transport),
    )

    async with extractor.create_http_client() as client:
        response = await client.get("https://any-url/test")
        data = response.json()

    assert response.status_code == 200
    assert data == {"ok": True}


@pytest.mark.asyncio
async def test_get_categories_of_products():
    fake_categories = [
        {"id": "cat_1", "title": "Fruits"},
        {"id": "cat_2", "title": "Vegetables"},
    ]

    def mock_handler(request: Request) -> Response:
        assert request.url.path == "/stores/store_123/categories"
        return Response(200, json=fake_categories)

    transport = make_mock_transport(mock_handler)
    async with httpx.AsyncClient(base_url="http://testserver", transport=transport) as client:
        categories = await extractor.get_categories_of_products("store_123", client=client)

    assert len(categories) == 2
    assert all(isinstance(c, Category) for c in categories)
    assert categories[0].id == "cat_1"
    assert categories[1].title == "Vegetables"


@pytest.mark.asyncio
async def test_search_products_with_category():
    fake_data_pages = {
        1: {"results": [{"ean": "111", "title": "Apple", "category_id": "cat_1"}]},
        2: {"results": []},
    }

    def mock_handler(request: Request) -> Response:
        page = int(request.url.params.get("page", "1"))
        return Response(200, json=fake_data_pages[page])

    transport = make_mock_transport(mock_handler)
    async with httpx.AsyncClient(base_url="http://testserver", transport=transport) as client:
        products = await extractor.search_products_with_category(
            "store_123", "cat_1", client=client
        )

    assert len(products) == 1
    p = products[0]
    assert isinstance(p, Product)
    assert p.ean == "111"
    assert p.category_id == "cat_1"


@pytest.mark.asyncio
async def test_search_products_with_category_http_error():
    def mock_handler(request: Request) -> Response:
        return Response(500, json={"detail": "Internal error"})

    transport = make_mock_transport(mock_handler)
    async with httpx.AsyncClient(base_url="http://testserver", transport=transport) as client:
        with pytest.raises(httpx.HTTPStatusError):
            await extractor.search_products_with_category("store_123", "cat_1", client=client)


@pytest.mark.asyncio
async def test_extract_data(monkeypatch):
    fake_categories = [
        {"id": "cat_1", "title": "Fruits"},
        {"id": "cat_2", "title": "Vegetables"},
    ]
    fake_products = {
        "cat_1": [{"ean": "111", "title": "Apple", "category_id": "cat_1"}],
        "cat_2": [{"ean": "222", "title": "Tomato", "category_id": "cat_2"}],
    }

    request_counts = {"cat_1": 0, "cat_2": 0}

    def mock_handler(request: Request) -> Response:
        path = request.url.path

        if path.endswith("/categories"):
            return Response(200, json=fake_categories)

        elif "/products/" in path:
            category_id = path.split("/")[-3]
            request_counts[category_id] += 1

            if request_counts[category_id] == 1:
                return Response(200, json={"results": fake_products.get(category_id, [])})
            else:
                return Response(200, json={"results": []})

        return Response(404, json={"detail": "Not found"})

    transport = MockTransport(mock_handler)

    @asynccontextmanager
    async def mock_create_http_client():
        client = httpx.AsyncClient(
            base_url="http://testserver",
            headers=DEFAULT_HEADERS,
            timeout=60,
            transport=transport,
        )
        try:
            yield client
        finally:
            await client.aclose()

    monkeypatch.setattr(extractor, "create_http_client", mock_create_http_client)

    products = await extractor.extract_data("store_123")

    assert isinstance(products, list)
    assert len(products) == 2

    eans = {p.ean for p in products}
    cats = {p.category_id for p in products}

    assert eans == {"111", "222"}
    assert cats == {"cat_1", "cat_2"}
