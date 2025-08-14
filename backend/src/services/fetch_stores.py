import httpx

from core.config import Settings

settings = Settings()

BASE_URL = settings.zakaz_api_base_url
USER_AGENT = settings.user_agent
HEADERS = {"User-Agent": USER_AGENT, "Accept": "application/json"}


async def async_fetch_stores() -> list[dict]:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/stores", headers=HEADERS)
        response.raise_for_status()
        stores = response.json()
        return [{"id": store["id"], "name": store["name"]} for store in stores]
