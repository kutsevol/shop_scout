from pydantic import BaseModel, Field


class Discount(BaseModel):
    status: bool | None = Field(default=None)
    value: int | None = Field(default=None)
    old_price: int | None = Field(default=None)
    due_date: str | None = Field(default=None)
