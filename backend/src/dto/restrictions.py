from pydantic import BaseModel


class Restrictions(BaseModel):
    in_sell_from: str  # "00:00"
    prohibited_payment_methods: list  # []
    available_for_delivery_services: list  # []
