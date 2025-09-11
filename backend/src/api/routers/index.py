from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["/"])
async def read_index() -> dict:
    return {"Hello": "Shop Scout is running"}
