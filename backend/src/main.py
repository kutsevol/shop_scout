import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import countries, index, shops
from core.logging_config import log_config

app = FastAPI()
app.include_router(index.router)
app.include_router(shops.router)
app.include_router(countries.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=log_config)
