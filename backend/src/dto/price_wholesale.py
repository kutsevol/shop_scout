from pydantic import BaseModel, Field


class PriceWholesale(BaseModel):
    min_qty: int | None = Field(default=None)
    price: int | None = Field(default=None)
    due_date: str | None = Field(default=None)
