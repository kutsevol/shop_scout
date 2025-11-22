import pytest
from polyfactory.factories.pydantic_factory import ModelFactory

from dto.product import Product
from pipeline.transform.transform import (
    transform_data,
)


class ProductFactory(ModelFactory[Product]):
    __model__ = Product


@pytest.mark.parametrize(
    "override,expected",
    [
        (
            {
                "ean": "1234567890123",
                "title": "Test Product",
                "category_id": "CAT1",
                "store_id": 1,
                "price": 10,
            },
            {
                "products": 1,
                "categories": 1,
                "prices": 1,
            },
        ),
        (
            {
                "ean": "1234567890123",
                "title": "Test Product",
                "category_id": "CAT1",
                "store_id": 2,
                "price": 20,
            },
            {
                "products": 1,
                "categories": 1,
                "prices": 1,
            },
        ),
        (
            {
                "ean": "5555555555555",
                "title": "Another Product",
                "category_id": "CAT2",
                "store_id": 1,
                "price": 30,
            },
            {
                "products": 1,
                "categories": 1,
                "prices": 1,
            },
        ),
    ],
)
def test_transform_valid_single(override, expected):
    product = ProductFactory.build(**override)

    result = transform_data([product])

    assert len(result["products"]) == expected["products"]
    assert len(result["categories"]) == expected["categories"]
    assert len(result["prices"]) == expected["prices"]

    prod = result["products"][0]
    cat = result["categories"][0]
    price = result["prices"][0]

    assert prod["ean"] == override["ean"]
    assert prod["category_id"] == override["category_id"]
    assert prod["store_id"] == override["store_id"]
    assert prod["title"].strip() == override["title"].strip()

    assert cat["id"] == override["category_id"]
    assert cat["store_id"] == str(override["store_id"])

    assert price["price"] == override["price"]


@pytest.mark.parametrize(
    "override,expected",
    [
        ({"ean": None}, {"products": [], "categories": [], "prices": []}),
        ({"title": None}, {"products": [], "categories": [], "prices": []}),
        ({"category_id": None}, {"products": [], "categories": [], "prices": []}),
        ({"price": None}, {"products": [], "categories": [], "prices": []}),
        ({"store_id": None}, {"products": [], "categories": [], "prices": []}),
    ],
)
def test_invalid_product_skipped(override, expected):
    product = ProductFactory.build(**override)
    result = transform_data([product])

    assert result["products"] == expected["products"]
    assert result["categories"] == expected["categories"]
    assert result["prices"] == expected["prices"]


@pytest.mark.parametrize(
    "p1,p2,expected",
    [
        (
            ProductFactory.build(ean="111", store_id=1, title="Prod A", category_id="A", price=10),
            ProductFactory.build(ean="111", store_id=1, title="Prod A", category_id="B", price=20),
            "A, B",
        )
    ],
)
def test_categories_accumulate(p1, p2, expected):
    result = transform_data([p1, p2])

    assert len(result["products"]) == 1

    assert result["products"][0]["categories"] == expected


@pytest.mark.parametrize(
    "p1,p2,expected",
    [
        (
            ProductFactory.build(
                ean="222", store_id=5, category_id="X", title="Product X", price=50
            ),
            ProductFactory.build(
                ean="999", store_id=5, category_id="Y", title="Product Y", price=100
            ),
            {"X", "Y"},
        )
    ],
)
def test_unique_categories(p1, p2, expected):
    result = transform_data([p1, p2])

    assert len(result["categories"]) == 2

    category_ids = {cat["id"] for cat in result["categories"]}
    assert category_ids == expected


@pytest.mark.parametrize(
    "p1,p2,expected",
    [
        (
            ProductFactory.build(ean="100", store_id=1, category_id="A", title="AAA", price=199),
            ProductFactory.build(ean="100", store_id=2, category_id="A", title="AAA", price=299),
            {199, 299},
        )
    ],
)
def test_prices_created_per_ean_store(p1, p2, expected):
    result = transform_data([p1, p2])

    prices = {pr["price"] for pr in result["prices"]}

    assert prices == expected
