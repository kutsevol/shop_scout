import httpx

# from config import Settings

# settings = Settings()

BASE_URL = "https://stores-api.zakaz.ua"
USER_AGENT = "price-checker/0.1 (+github.com/you)"
HEADERS = {"User-Agent": USER_AGENT, "Accept": "application/json"}


async def async_fetch_stores() -> list[dict]:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/stores", headers=HEADERS)
        response.raise_for_status()
        stores = response.json()
        return [{"id": store["id"], "name": store["name"]} for store in stores]
