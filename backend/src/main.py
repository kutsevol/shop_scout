import uvicorn
from fastapi import FastAPI

from api.routers import countries, index, shops

app = FastAPI()

app.include_router(index.router)
app.include_router(shops.router)
app.include_router(countries.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
