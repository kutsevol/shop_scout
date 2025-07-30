import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Store(BaseModel):
    id: int
    name: str


@app.get("/")
def read_index():
    return {"Hello": "App"}


stores = [Store(id=1, name="Auchan"), Store(id=2, name="Metro")]


@app.get("/stores")
def read_stores():
    return stores


@app.get("/store/{store_id}")
def read_store(store_id: int):
    for store in stores:
        if store.id == store_id:
            return {"id": store.id, "name": store.name}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
