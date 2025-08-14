from fastapi import APIRouter, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from dto.product import Product
from dto.shop import Shop
from services.fetch_stores import fetch_stores
from services.search_products import search_products

router = APIRouter(prefix="/shops", tags=["shops"])


@router.get("/", response_model=list[Shop])
async def get_shops() -> JSONResponse:
    stores = await fetch_stores()
    shops = [Shop(**store) for store in stores]
    return JSONResponse(content=jsonable_encoder(shops))


@router.get("/{shop_id}/", response_model=Shop)
async def get_shop(shop_id: str) -> JSONResponse:
    stores = await fetch_stores()
    shops = [Shop(**store) for store in stores]
    for shop in shops:
        if shop.id == shop_id:
            return JSONResponse(content=jsonable_encoder(shop))
    raise HTTPException(status_code=404, detail="Not Found")


@router.get("/{shop_id}/search/", response_model=list[Product])
async def get_product_from_shop(
    shop_id: str, product: str = Query(..., description="Product name to search for")
) -> JSONResponse:
    results = await search_products(store_id=shop_id, query=product)
    products = [Product(**product) for product in results]
    return JSONResponse(content=jsonable_encoder(products))
