from fastapi import APIRouter, HTTPException

from dto.country import Country
from dto.shop import Shop
from static import async_fetch_stores, async_search_products, countries

router = APIRouter()


@router.get("/", tags=["/"])
async def read_index() -> dict:
    return {"Hello": "App"}


@router.get("/shops/", tags=["shops"])
async def read_shops() -> list[Shop]:
    stores = await async_fetch_stores()
    shops = [Shop(**store) for store in stores]
    return shops


@router.get("/countries/", tags=["countries"])
async def get_countries() -> list[Country]:
    return countries


@router.get("/shop/{shop_id}/", tags=["shop"])
async def read_shop(shop_id: int) -> Shop | str:
    stores = await async_fetch_stores()
    shops = [Shop(**store) for store in stores]
    for shop in shops:
        if shop.id == shop_id:
            return shop
    raise HTTPException(status_code=404, detail="Not Found")


@router.get("/shop/{shop_id}/{product}/", tags=["products"])
async def read_shop2(shop_id: str, product: str) -> list[dict]:
    products = await async_search_products(store_id=shop_id, query=product)
    return products
