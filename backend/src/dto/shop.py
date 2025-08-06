from pydantic import BaseModel


class Shop(BaseModel):
    id: int
    name: str
