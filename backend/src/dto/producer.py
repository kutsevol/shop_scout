from pydantic import BaseModel

from dto.logo import Logo


class Producer(BaseModel):
    trademark: str  # "Квас Тарас"
    trademark_slug: str  # "kvas-taras"
    website: str  # "https://carlsbergukraine.com"
    logo: Logo
    name: str  # "\"carlsberg ukraine\" pjsc"
