from pydantic import BaseModel


class Restrictions(BaseModel):
    in_sell_from: str | None = None
    prohibited_payment_methods: list[str] | None = None
    available_for_delivery_services: list[str] | None = None
