from contextlib import asynccontextmanager
from typing import AsyncIterator

import httpx

from core.config import settings

BASE_URL = settings.zakaz_api_base_url
DEFAULT_HEADERS = {"Accept": "application/json"}


@asynccontextmanager
async def create_http_client(
    base_url: str = BASE_URL, headers: dict = DEFAULT_HEADERS, timeout: int = 60
) -> AsyncIterator[httpx.AsyncClient]:
    client = httpx.AsyncClient(
        base_url=base_url,
        headers=headers,
        timeout=timeout,
    )
    try:
        yield client
    finally:
        await client.aclose()
