from pydantic import BaseModel


class Quantity(BaseModel):
    min: int | None = None  # 1
    step: int | None = None  # 1
    is_strict: bool | None = None  # false
