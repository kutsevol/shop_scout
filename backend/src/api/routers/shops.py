import logging

from fastapi import APIRouter, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from dto.product import Product
from dto.shop import Shop
from services.fetch_stores import fetch_stores
from services.search_products import search_products

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/shops", tags=["shops"])


@router.get("/", response_model=list[Shop])
async def get_shops() -> JSONResponse:
    stores = await fetch_stores()
    logger.info(f"Fetched {len(stores)} stores")
    shops = [Shop(**store) for store in stores]
    return JSONResponse(content=jsonable_encoder(shops))


@router.get("/{shop_id}/", response_model=Shop)
async def get_shop(shop_id: str) -> JSONResponse:
    logger.info(f"Looking for shop with ID: {shop_id}")
    stores = await fetch_stores()
    shops = [Shop(**store) for store in stores]
    logger.info(f"Total shops fetched: {len(shops)}")
    for shop in shops:
        if shop.id == shop_id:
            logger.info(f"Shop found: {shop}")
            return JSONResponse(content=jsonable_encoder(shop))
    raise HTTPException(status_code=404, detail="Not Found")


@router.get("/{shop_id}/search/", response_model=list[Product])
async def get_product_from_shop(
    shop_id: str, product: str = Query(..., description="Product name to search for")
) -> JSONResponse:
    results = await search_products(store_id=shop_id, query=product)
    products = [Product(**product) for product in results]
    logger.info(f"Found {len(products)} products in shop {shop_id} for query '{product}'")
    return JSONResponse(content=jsonable_encoder(products))
