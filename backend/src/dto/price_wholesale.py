from pydantic import BaseModel


class PriceWholesale(BaseModel):
    min_qty: int | None = None
    price: int | None = None
    due_date: str | None = None
