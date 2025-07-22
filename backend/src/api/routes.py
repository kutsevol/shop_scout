from fastapi import APIRouter, HTTPException

from dto.shop import Shop
from static import shops

router = APIRouter()


@router.get("/", tags=["/"])
async def read_index() -> dict:
    return {"Hello": "App"}


@router.get("/shops/", tags=["shops"])
async def read_shops() -> list[Shop]:
    return shops


@router.get("/shop/{shop_id}/", tags=["shop"])
async def read_shop(shop_id: int) -> Shop | str:
    for shop in shops:
        if shop.id == shop_id:
            return shop
    raise HTTPException(status_code=404, detail="Not Found")
