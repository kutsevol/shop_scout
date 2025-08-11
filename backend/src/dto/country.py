from pydantic import BaseModel


class Country(BaseModel):
    id: int
    name: str
    code: str
    emoji: str
    unicode: str
    image: str
