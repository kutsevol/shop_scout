from pydantic import BaseModel, Field


class Restrictions(BaseModel):
    in_sell_from: str | None = Field(default=None)
    prohibited_payment_methods: list[str] | None = Field(default=None)
    available_for_delivery_services: list[str] | None = Field(default=None)
