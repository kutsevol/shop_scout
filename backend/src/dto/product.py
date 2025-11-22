from typing import Any

from pydantic import BaseModel, Field, field_validator


class Product(BaseModel):
    ean: str | None = Field(default=None)
    title: str | None = Field(default=None)
    price: int | None = Field(default=None)
    category_id: str | None = Field(default=None)
    producer: str | None = Field(default=None)
    store_id: str | int | None = Field(default=None)

    @field_validator("producer", mode="before")
    def normalize_producer(cls, v: Any) -> str | None:
        if isinstance(v, dict):
            return v.get("trademark")
        return v
