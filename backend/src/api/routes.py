from fastapi import HTTPException

from fastapi import APIRouter, FastAPI
import json
import pathlib
from models.models import Store


app = FastAPI()
router = APIRouter()


base_dir = pathlib.Path(__file__).resolve().parent.parent.parent
stores_path = base_dir / "data" / "stores.json"
stores_json = json.loads(stores_path.read_text())
stores = []
for store in stores_json:
    stores.append(Store(**store))


@router.get("/")
async def read_index() -> dict:
    return {"Hello": "App"}


@router.get("/stores/", tags=["stores"])
async def read_stores() -> list[Store]:
    return stores


@router.get("/store/{store_id}/")
async def read_store(store_id: int) -> Store | str:
    for store in stores:
        if store.id == store_id:
            return store
    raise HTTPException(status_code=404, detail="Store not found")
