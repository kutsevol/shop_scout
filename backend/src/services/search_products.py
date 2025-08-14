import httpx

from core.config import Settings

settings = Settings()

BASE_URL = settings.zakaz_api_base_url
USER_AGENT = settings.user_agent
HEADERS = {"User-Agent": USER_AGENT, "Accept": "application/json"}


async def async_search_products(store_id: str, query: str) -> list[dict]:
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}/stores/{store_id}/products/search/"
        headers = HEADERS.copy()
        params = {"q": query}

        try:
            response = await client.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            results = data.get("results", [])
            for product in results:
                product["store_id"] = store_id
            return results
        except httpx.RequestError as e:
            print(f"Request error for store {store_id}: {e}")
            return []
        except httpx.HTTPStatusError as e:
            print(f"HTTP error for store {store_id}: {e}")
            return []
