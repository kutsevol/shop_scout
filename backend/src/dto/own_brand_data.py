from pydantic import BaseModel, Field


class OwnBrandData(BaseModel):
    name: str | None = Field(default=None)
