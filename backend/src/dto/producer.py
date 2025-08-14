from pydantic import BaseModel, Field

from dto.logo import Logo


class Producer(BaseModel):
    trademark: str | None = Field(default=None)
    trademark_slug: str | None = Field(default=None)
    website: str | None = Field(default=None)
    logo: Logo | None = Field(default=None)
    name: str | None = Field(default=None)
