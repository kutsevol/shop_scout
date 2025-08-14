from pydantic import BaseModel, Field


class Logo(BaseModel):
    small_url: str | None = Field(default=None, alias="s16x16")
    medium_url: str | None = Field(default=None, alias="s32x32")
    large_url: str | None = Field(default=None, alias="s64x64")
