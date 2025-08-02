from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Store(BaseModel):
    id: int
    name: str
