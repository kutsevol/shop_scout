import logging

import httpx

from core.config import settings

BASE_URL = settings.zakaz_api_base_url
HEADERS = {"Accept": "application/json"}


async def search_products(store_id: str, query: str, page: int) -> list[dict]:
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}/stores/{store_id}/products/search/"
        params: dict[str, str | int] = {"q": query, "page": page}

        try:
            response = await client.get(url, headers=HEADERS, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            results = data.get("results", [])
            for product in results:
                product["store_id"] = store_id
            return results
        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            logging.error(f"Failed to search products in store {store_id} for query '{query}': {e}")
            raise
