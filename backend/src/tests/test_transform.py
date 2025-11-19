import pytest

from dto.product import Product
from pipeline.transform.transform import (
    ProductEntity,
    ProductPriceEntity,
    transform_data,
)


def make_product(
    ean="123",
    title="Test",
    price=10000,
    category_id="cat",
    country="UA",
    store_id="1",
):
    return Product(
        ean=ean,
        title=title,
        price=price,
        category_id=category_id,
        country=country,
        store_id=store_id,
    )


def test_transform_basic():
    products = [
        make_product(ean="111", price=23900, category_id="meat"),
        make_product(ean="222", price=15000, category_id="milk"),
    ]

    result = transform_data(products, latest_prices={})

    assert len(result["products"]) == 2
    assert len(result["categories"]) == 2
    assert len(result["prices"]) == 2

    p1 = result["products"][0]
    assert isinstance(p1, ProductEntity)


def test_price_normalization():
    product = make_product(ean="111", price=23900)
    result = transform_data([product], latest_prices={})
    price_record = result["prices"][0]

    assert price_record.price == pytest.approx(239.00)


def test_unique_products_by_ean():
    p1 = make_product(ean="111", title="A")
    p2 = make_product(ean="111", title="A")

    result = transform_data([p1, p2], latest_prices={})

    assert len(result["products"]) == 1
    assert len(result["prices"]) == 1


def test_categories_are_unique():
    p1 = make_product(category_id="meat")
    p2 = make_product(category_id="meat")

    result = transform_data([p1, p2], latest_prices={})

    assert len(result["categories"]) == 1


def test_price_versioning_no_change():
    p = make_product(ean="111", price=23800)

    latest_prices = {"111": 238.00}

    result = transform_data([p], latest_prices)

    assert len(result["prices"]) == 0


def test_price_versioning_with_change():
    p = make_product(ean="111", price=23900)

    latest_prices = {"111": 238.00}

    result = transform_data([p], latest_prices)

    assert len(result["prices"]) == 1
    assert isinstance(result["prices"][0], ProductPriceEntity)


def test_invalid_rows_are_skipped():
    p1 = make_product(ean="", title="X")
    p2 = make_product(ean="111", title="")
    p3 = make_product(ean="222", category_id="")

    result = transform_data([p1, p2, p3], latest_prices={})

    assert len(result["products"]) == 0
    assert len(result["prices"]) == 0
    assert len(result["categories"]) == 0


def test_strip_fields():
    p = make_product(
        ean="  111  ",
        title="  Test Product ",
        category_id="  cat1 ",
    )

    result = transform_data([p], latest_prices={})
    product = result["products"][0]

    assert product.ean == "111"
    assert product.title == "Test Product"
    assert product.category_id == "cat1"
