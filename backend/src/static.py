from typing import List

import httpx

from dto.country import Country

BASE_URL = "https://stores-api.zakaz.ua"
HEADERS = {"User-Agent": "price-checker/0.1 (+github.com/you)", "Accept": "application/json"}


async def async_fetch_stores() -> List[dict]:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/stores", headers=HEADERS)
        response.raise_for_status()
        stores = response.json()
        return [{"id": store["id"], "name": store["name"]} for store in stores]


async def async_search_products(store_id: str, query: str) -> List[dict]:
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}/stores/{store_id}/products/search/"
        headers = HEADERS.copy()
        # headers["x-chain"] = store_id
        # headers["x-chain"] = "tavriav"
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


# async def main1():
#     stores = await async_fetch_stores()
#     shops = [Shop(**store) for store in stores]
#     print(shops)
#     return shops

# print(shops)
# for shop in shops:
#     print(shop)
# store_ids = [stores[i]["id"] for i in range(len(stores))]
# store_names = [stores[i]["name"] for i in range(len(stores))]
# print(f"Отримано {len(stores)} магазинів")
# print(stores[0])
# async with httpx.AsyncClient() as client:
#     bread = await async_search_products(client=client, store_id=store_ids[0], query="potato")
# print(bread)

# shops = asyncio.run(main1())
# 482010105

countries = [
    Country(
        id=1,
        name="Ukraine",
        code="UA",
        emoji="🇺🇦",
        unicode="U+1F1FA U+1F1E6",
        image="https://cdn.jsdelivr.net/npm/country-flag-emoji-json@2.0.0/dist/images/UA.svg",
    ),
    Country(
        id=2,
        name="France",
        code="FR",
        emoji="🇫🇷",
        unicode="U+1F1EB U+1F1F7",
        image="https://cdn.jsdelivr.net/npm/country-flag-emoji-json@2.0.0/dist/images/FR.svg",
    ),
    Country(
        id=3,
        name="Spain",
        code="ES",
        emoji="🇪🇸",
        unicode="U+1F1EA U+1F1F8",
        image="https://cdn.jsdelivr.net/npm/country-flag-emoji-json@2.0.0/dist/images/ES.svg",
    ),
    Country(
        id=4,
        name="Germany",
        code="DE",
        emoji="🇩🇪",
        unicode="U+1F1E9 U+1F1EA",
        image="https://cdn.jsdelivr.net/npm/country-flag-emoji-json@2.0.0/dist/images/DE.svg",
    ),
]
