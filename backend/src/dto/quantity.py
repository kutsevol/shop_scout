from pydantic import BaseModel


class Quantity(BaseModel):
    min: int | None = None
    step: int | None = None
    is_strict: bool | None = None
