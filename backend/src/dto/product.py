from pydantic import BaseModel, Field


class Product(BaseModel):
    ean: str | None = Field(default=None)
    title: str | None = Field(default=None)
    price: int | None = Field(default=None)
    category_id: str | None = Field(default=None)
    country: str | None = Field(default=None)
    store_id: str | None = Field(default=None)
