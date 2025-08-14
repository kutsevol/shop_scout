import httpx

from core.config import AppSettings

settings = AppSettings()

BASE_URL = settings.zakaz_api_base_url
HEADERS = {"Accept": "application/json"}


async def fetch_stores() -> list[dict]:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/stores", headers=HEADERS)
        response.raise_for_status()
        stores = response.json()
        return [{"id": store["id"], "name": store["name"]} for store in stores]
