from typing import Any, TypedDict

from dto.product import Product


class ProductEntity(TypedDict):
    ean: str
    title: str
    category_id: str
    producer: str | None
    store_id: str | int
    categories: str


class CategoryEntity(TypedDict):
    id: str | int
    store_id: str


class ProductPriceEntity(TypedDict):
    ean: str
    store_id: str | int
    price: int


class TransformResult(TypedDict):
    products: list[ProductEntity]
    categories: list[CategoryEntity]
    prices: list[ProductPriceEntity]
    links: list[dict[str, Any]]


def transform_data(
    products: list[Product],
) -> TransformResult:
    product_entities = {}
    category_entities = {}
    price_entities = {}

    for p in products:
        if (
            p.store_id is None
            or p.ean is None
            or p.title is None
            or p.category_id is None
            or p.price is None
        ):
            continue

        ean = str(p.ean).strip()
        title = p.title.strip()
        price = p.price
        category_id = p.category_id.strip()
        producer = str(p.producer).strip() if p.producer else None

        category_key = (category_id, str(p.store_id))
        if category_key not in category_entities:
            category_entities[category_key] = CategoryEntity(
                id=category_id,
                store_id=str(p.store_id),
            )

        key = (ean, str(p.store_id))
        if key not in product_entities:
            product_entities[key] = ProductEntity(
                ean=ean,
                title=title,
                category_id=category_id,
                producer=producer,
                store_id=p.store_id,
                categories=category_id,
            )
        else:
            product_entities[key]["categories"] += f", {category_id}"

        if key not in price_entities:
            price_entities[key] = ProductPriceEntity(
                ean=ean,
                store_id=p.store_id,
                price=price,
            )

    return {
        "products": list(product_entities.values()),
        "categories": list(category_entities.values()),
        "prices": list(price_entities.values()),
        "links": [],
    }
