from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from dto.country import Country
from static import countries

router = APIRouter(prefix="/countries", tags=["countries"])


@router.get("/", response_model=list[Country])
async def get_countries() -> JSONResponse:
    return JSONResponse(content=jsonable_encoder(countries))
