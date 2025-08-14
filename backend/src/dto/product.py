from pydantic import BaseModel, Field

from dto.discount import Discount
from dto.img import Img
from dto.nutrition_facts import NutritionFacts
from dto.own_brand_data import OwnBrandData
from dto.price_wholesale import PriceWholesale
from dto.producer import Producer
from dto.quantity import Quantity
from dto.restrictions import Restrictions


class Product(BaseModel):
    ean: str | None = Field(default=None)
    sku: str | None = Field(default=None)
    title: str | None = Field(default=None)
    price: int | None = Field(default=None)
    price_wholesale: list[PriceWholesale] | None = Field(default=None)
    discount: Discount | None = Field(default=None)
    bundle: int | None = Field(default=None)
    unit: str | None = Field(default=None)
    volume: float | None = Field(default=None)
    quantity: Quantity | None = Field(default=None)
    currency: str | None = Field(default=None)
    category_id: str | None = Field(default=None)
    parent_category_id: str | None = Field(default=None)
    category_filters: list[str] | None = Field(default=None)
    description: str | None = Field(default=None)
    nutrition_facts: NutritionFacts | None = Field(default=None)
    slug: str | None = Field(default=None)
    in_stock: bool | None = Field(default=None)
    is_hit: bool | None = Field(default=None)
    is_alcohol: bool | None = Field(default=None)
    is_nicotine: bool | None = Field(default=None)
    is_ready_meal: bool | None = Field(default=None)
    is_new_product: bool | None = Field(default=None)
    horeca_only: bool | None = Field(default=None)
    excisable: bool | None = Field(default=None)
    web_url: str | None = Field(default=None)
    restrictions: Restrictions | None = Field(default=None)
    ingredients: list[str] | None = Field(default=None)
    fat: str | None = Field(default=None)
    shelf_life: str | None = Field(default=None)
    temperature_range: str | None = Field(default=None)
    pack_amount: int | None = Field(default=None)
    country: str | None = Field(default=None)
    producer: Producer | None = Field(default=None)
    custom_ribbons: list[str] | None = Field(default=None)
    img: Img | None = Field(default=None)
    gallery: list[Img] | None = Field(default=None)
    is_uber_item: bool | None = Field(default=None)
    verbose_stock: str | None = Field(default=None)
    take_more: bool | None = Field(default=None)
    is_own_brand: bool | None = Field(default=None)
    available_for_cart: bool | None = Field(default=None)
    own_brand_data: OwnBrandData | None = Field(default=None)
    taxons: list[str] | None = Field(default=None)
    weight: float | None = Field(default=None)
    has_similar_products: str | None = Field(default=None)
    hits: int | None = Field(default=None)
    shopping_list_count: str | None = Field(default=None)
    store_id: str | None = Field(default=None)
