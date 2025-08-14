from pydantic import BaseModel

from dto.discount import Discount
from dto.img import Img
from dto.nutrition_facts import NutritionFacts
from dto.own_brand_data import OwnBrandData
from dto.price_wholesale import PriceWholesale
from dto.producer import Producer
from dto.quantity import Quantity
from dto.restrictions import Restrictions


class Product(BaseModel):
    ean: str | None = None
    sku: str | None = None
    title: str | None = None
    price: int | None = None
    price_wholesale: list[PriceWholesale] | None = None
    discount: Discount | None = None
    bundle: int | None = None
    unit: str | None = None
    volume: float | None = None
    quantity: Quantity | None = None
    currency: str | None = None
    category_id: str | None = None
    parent_category_id: str | None = None
    category_filters: list[str] | None = None
    description: str | None = None
    nutrition_facts: NutritionFacts | None = None
    slug: str | None = None
    in_stock: bool | None = None
    is_hit: bool | None = None
    is_alcohol: bool | None = None
    is_nicotine: bool | None = None
    is_ready_meal: bool | None = None
    is_new_product: bool | None = None
    horeca_only: bool | None = None
    excisable: bool | None = None
    web_url: str | None = None
    restrictions: Restrictions | None = None
    ingredients: list[str] | None = None
    fat: str | None = None
    shelf_life: str | None = None
    temperature_range: str | None = None
    pack_amount: int | None = None
    country: str | None = None
    producer: Producer | None = None
    custom_ribbons: list[str] | None = None
    img: Img | None = None
    gallery: list[Img] | None = None
    is_uber_item: bool | None = None
    verbose_stock: str | None = None
    take_more: bool | None = None
    is_own_brand: bool | None = None
    available_for_cart: bool | None = None
    own_brand_data: OwnBrandData | None = None
    taxons: list[str] | None = None
    weight: float | None = None
    has_similar_products: str | None = None
    hits: int | None = None
    shopping_list_count: str | None = None
    store_id: str | None = None
