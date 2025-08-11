from pydantic import BaseModel


class Discount(BaseModel):
    status: bool  # false
    value: int  # 0
    old_price: int  # 6799
    due_date: str  # null
