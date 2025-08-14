from pydantic import BaseModel


class Discount(BaseModel):
    status: bool | None = None
    value: int | None = None
    old_price: int | None = None
    due_date: str | None = None
