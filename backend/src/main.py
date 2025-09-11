import uvicorn
from fastapi import FastAPI

from api.routers import countries, index, shops
from core.config import settings
from core.logging_config import log_config

servers = [{"url": settings.root_path, "description": "Production"}]


app = FastAPI(
    title="Shop Scout API",
    root_path=settings.root_path,
    servers=servers,
)
app.include_router(index.router)
app.include_router(shops.router)
app.include_router(countries.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=log_config)
