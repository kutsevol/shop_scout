from pydantic import BaseModel, Field


class Quantity(BaseModel):
    min: int | None = Field(default=None)
    step: int | None = Field(default=None)
    is_strict: bool | None = Field(default=None)
