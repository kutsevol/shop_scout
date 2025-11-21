import pytest
from polyfactory.factories.pydantic_factory import ModelFactory

from dto.product import Product
from pipeline.transform.transform import (
    transform_data,
)


class ProductFactory(ModelFactory[Product]):
    __model__ = Product


@pytest.mark.parametrize(
    "override",
    [
        # base valid product
        {
            "ean": "1234567890123",
            "title": "Test Product",
            "category_id": "CAT1",
            "store_id": 1,
            "price": 10,
        },
        # another store
        {
            "ean": "1234567890123",
            "title": "Test Product",
            "category_id": "CAT1",
            "store_id": 2,
            "price": 20,
        },
        # another ean
        {
            "ean": "5555555555555",
            "title": "Another Product",
            "category_id": "CAT2",
            "store_id": 1,
            "price": 30,
        },
    ],
)
def test_transform_valid_single(override):
    product: Product = ProductFactory.build(**override)

    result = transform_data([product])

    assert len(result["products"]) == 1
    assert len(result["categories"]) == 1
    assert len(result["prices"]) == 1

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
    "override",
    [
        {"ean": None},
        {"title": None},
        {"category_id": None},
        {"price": None},
        {"store_id": None},
    ],
)
def test_invalid_product_skipped(override):
    product: Product = ProductFactory.build(**override)
    result = transform_data([product])

    assert result["products"] == []
    assert result["categories"] == []
    assert result["prices"] == []


def test_categories_accumulate():
    p1 = ProductFactory.build(ean="111", store_id=1, title="Prod A", category_id="A", price=10)
    p2 = ProductFactory.build(ean="111", store_id=1, title="Prod A", category_id="B", price=20)

    result = transform_data([p1, p2])

    products = result["products"]
    assert len(products) == 1

    assert products[0]["categories"] == "A, B"


def test_unique_categories():
    p1 = ProductFactory.build(ean="222", store_id=5, category_id="X", title="Product X", price=50)
    p2 = ProductFactory.build(ean="999", store_id=5, category_id="Y", title="Product Y", price=100)

    result = transform_data([p1, p2])

    assert len(result["categories"]) == 2

    category_ids = {cat["id"] for cat in result["categories"]}
    assert category_ids == {"X", "Y"}


def test_prices_created_per_ean_store():
    p1 = ProductFactory.build(ean="100", store_id=1, category_id="A", title="AAA", price=199)
    p2 = ProductFactory.build(ean="100", store_id=2, category_id="A", title="AAA", price=299)

    result = transform_data([p1, p2])

    prices = result["prices"]

    assert len(prices) == 2
    assert {pr["price"] for pr in prices} == {199, 299}
