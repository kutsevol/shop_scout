import logging

import httpx

from core.config import settings

logger = logging.getLogger(__name__)
BASE_URL = settings.zakaz_api_base_url
HEADERS = {"Accept": "application/json"}


async def fetch_stores() -> list[dict]:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/stores", headers=HEADERS)
        logger.debug(f"Fetching stores from {BASE_URL}/stores")
        response.raise_for_status()
        stores = response.json()
        logger.debug(f"Fetched {len(stores)} stores")
        return [{"id": store["id"], "name": store["name"]} for store in stores]
