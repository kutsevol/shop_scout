from pydantic import BaseModel, Field


class Category(BaseModel):
    id: str = Field()
    title: str | None = Field(default=None)
