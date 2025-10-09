from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["/"])
async def read_index() -> dict:
    return {"Hello": "Shop Scout is running"}


@router.get("/health-check")
async def health_check() -> dict:
    return {"status": "ok"}
