from pydantic import BaseModel


class Shop(BaseModel):
    id: str
    name: str
