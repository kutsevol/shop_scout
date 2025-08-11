from pydantic import BaseModel


class Quantity(BaseModel):
    min: int  # 1
    step: int  # 1
    is_strict: bool  # false
