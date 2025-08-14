from pydantic import BaseModel, Field


class Img(BaseModel):
    small_url: str | None = Field(default=None, alias="s150x150")
    medium_url: str | None = Field(default=None, alias="s200x200")
    large_url: str | None = Field(default=None, alias="s350x350")
    very_large_url: str | None = Field(default=None, alias="s1350x1350")
