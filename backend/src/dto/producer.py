from pydantic import BaseModel

from dto.logo import Logo


class Producer(BaseModel):
    trademark: str | None = None  # "Квас Тарас"
    trademark_slug: str | None = None  # "kvas-taras"
    website: str | None = None  # "https://carlsbergukraine.com"
    logo: Logo | None = None
    name: str | None = None  # "\"carlsberg ukraine\" pjsc"
