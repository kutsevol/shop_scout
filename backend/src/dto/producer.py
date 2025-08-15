from pydantic import BaseModel

from dto.logo import Logo


class Producer(BaseModel):
    trademark: str | None = None
    trademark_slug: str | None = None
    website: str | None = None
    logo: Logo | None = None
    name: str | None = None
