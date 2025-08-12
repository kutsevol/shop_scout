from pydantic import BaseModel


class Discount(BaseModel):
    status: bool | None = None  # false
    value: int | None = None  # 0
    old_price: int | None = None  # 6799
    due_date: str | None = None  # null
