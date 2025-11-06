import asyncio
import logging

import httpx

from dto.category import Category
from dto.product import Product
from pipeline.extractor.client import create_http_client


async def get_categories_of_products(
    store_id: str,
    client: httpx.AsyncClient,
) -> list[Category]:
    response = await client.get(f"/stores/{store_id}/categories")
    response.raise_for_status()
    data = response.json()

    return [Category(**category) for category in data]


async def search_products_with_category(
    store_id: str,
    category_id: str,
    client: httpx.AsyncClient,
) -> list[Product]:
    url = f"/stores/{store_id}/categories/{category_id}/products/"
    all_results = []
    page = 1

    while True:
        response = await client.get(url, params={"page": page})
        response.raise_for_status()
        data = response.json()
        results = data.get("results", [])

        if not results:
            break

        all_results.extend(results)
        page += 1

    return [Product(**p, store_id=store_id) for p in all_results]


async def extract_data(store_id: str) -> list[Product]:
    try:
        async with create_http_client() as client:
            all_categories = await get_categories_of_products(store_id, client)

            tasks = [
                search_products_with_category(store_id, category.id, client)
                for category in all_categories
                if category.id
            ]

            logging.info(f"Fetching products for {len(tasks)} categories.")
            product_lists = await asyncio.gather(*tasks)
            all_products = [p for lst in product_lists for p in lst]
            logging.info(f"Extracted {len(all_products)} products in total.")
            return all_products

    except (httpx.RequestError, httpx.HTTPStatusError, ValueError) as e:
        logging.error(f"Data extraction failed for store {store_id}: {e}")
        raise
