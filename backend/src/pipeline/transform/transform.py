from dataclasses import dataclass
from datetime import datetime

from dto.product import Product


@dataclass
class ProductEntity:
    ean: str
    title: str
    category_id: str
    country: str | None
    store_id: str | int


@dataclass
class CategoryEntity:
    id: str | int
    store_id: str


@dataclass
class ProductPriceEntity:
    ean: str
    store_id: str | int
    price: float
    date: datetime


def transform_data(
    products: list[Product], latest_prices: dict[str, float], load_date: datetime | None = None
) -> dict[str, list]:
    load_date = load_date or datetime.now()

    product_entities = {}
    categories = {}
    price_entities = []

    seen_prices_today = set()

    for p in products:
        if p.store_id is None:
            continue

        if not p.ean or not p.title or not p.category_id:
            continue

        if p.price is None:
            continue

        price = float(p.price) / 100 if isinstance(p.price, int) else float(p.price)

        ean = str(p.ean).strip()
        title = p.title.strip()
        category_id = p.category_id.strip()

        category_key = (category_id, str(p.store_id))
        if category_key not in categories:
            categories[category_key] = CategoryEntity(
                id=category_id,
                store_id=str(p.store_id),
            )

        product_key = (ean, str(p.store_id))
        if product_key not in product_entities:
            product_entities[product_key] = ProductEntity(
                ean=ean,
                title=title,
                category_id=category_id,
                country=p.country,
                store_id=p.store_id,
            )

        price_key = (ean, str(p.store_id))
        if price_key not in seen_prices_today:
            last_price = latest_prices.get(ean)

            if last_price is None or abs(float(last_price) - float(price)) > 0.001:
                price_entities.append(
                    ProductPriceEntity(
                        ean=ean,
                        store_id=p.store_id,
                        price=price,
                        date=load_date,
                    )
                )

            seen_prices_today.add(price_key)

    return {
        "products": list(product_entities.values()),
        "categories": list(categories.values()),
        "prices": price_entities,
    }
