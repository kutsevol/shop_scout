from pydantic import BaseModel


class Restrictions(BaseModel):
    in_sell_from: str | None = None  # "00:00"
    prohibited_payment_methods: list | None = None  # []
    available_for_delivery_services: list | None = None  # []
