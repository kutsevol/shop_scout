from pydantic import BaseModel

from dto.discount import Discount
from dto.img import Img
from dto.nutrition_facts import NutritionFacts
from dto.producer import Producer
from dto.quantity import Quantity
from dto.restrictions import Restrictions


class Product(BaseModel):
    ean: str | None = None  # "04820000451888"
    sku: str | None = None  # "6195"
    title: str | None = None  # "Kvas Taras Bread Kvas 2l"
    price: int | None = None  # 6799
    price_wholesale: list | None = None  # []
    discount: Discount | None = None
    bundle: int | None = None  # 1
    unit: str | None = None  # "pcs"
    volume: float | None = None  # 2000
    quantity: Quantity | None = None
    currency: str | None = None  # "uah"
    category_id: str | None = None  # "kvass-pasteurized-novus"
    parent_category_id: str | None = None  # "drinks"
    category_filters: list | None = None  # []
    description: str | None = (
        None  # "Highly carbonated pasteurized fermented drink. It has a refreshing sweet and sour taste with a touch of fresh rye bread. Available in several formats: PETF 0.5 l; 1l; 2l; 2.5l, keg 30l; 50l \nStore at temperatures from 0 ° C to 25 ° C. Light opalescence and sediment are allowed."
    )
    nutrition_facts: NutritionFacts | None = None
    slug: str | None = None  # "kvas-kvas-taras-2000ml"
    in_stock: bool | None = None  # true
    is_hit: bool | None = None  # false
    is_alcohol: bool | None = None  # false
    is_nicotine: bool | None = None  # false
    is_ready_meal: bool | None = None  # false
    is_new_product: bool | None = None  # false
    horeca_only: bool | None = None  # true
    excisable: bool | None = None  # false
    web_url: str | None = (
        None  # "https://novus.zakaz.ua/en/products/kvas-kvas-taras-2000ml--04820000451888/"
    )
    restrictions: Restrictions | None = None
    ingredients: list[str] | None = (
        None  # ["Drinking water, glucose-fructose syrup, barley, rye malt, barley malt, concentrate of leavened wort (rye flour, rye malt, barley malt), yeast, citric acid acidity regulator.\u003Cbr\u003E"]
    )
    fat: str | None = None  # null
    shelf_life: str | None = None  # "180 days"
    temperature_range: str | None = None  # "0...25"
    pack_amount: int | None = None  # null
    country: str | None = None  # "Ukraine"
    producer: Producer | None = None
    custom_ribbons: list | None = None  # []
    img: Img | None = None
    gallery: list[dict] | None = None  # [{
    #    "s150x150": "https://img3.zakaz.ua/5b365cbefa4846ef9ea45bdbfc3a1fef/1754296399-s150x150.jpg",
    #    "s200x200": "https://img3.zakaz.ua/5b365cbefa4846ef9ea45bdbfc3a1fef/1754296399-s200x200.jpg",
    #    "s350x350": "https://img3.zakaz.ua/5b365cbefa4846ef9ea45bdbfc3a1fef/1754296399-s350x350.jpg",
    #    "s1350x1350": "https://img2.zakaz.ua/5b365cbefa4846ef9ea45bdbfc3a1fef/1754296399-s1350x1350.jpg"
    # }]
    is_uber_item: bool | None = None  # false
    verbose_stock: str | None = None  # "low_stock"
    take_more: bool | None = None  # false
    is_own_brand: bool | None = None  # false
    available_for_cart: bool | None = None  # true
    own_brand_data: dict | None = None  # {}
    taxons: list | None = None  # []
    weight: float | None = None  # null
    has_similar_products: str | None = None  # null
    hits: int | None = None  # 2
    shopping_list_count: str | None = None  # null
    store_id: str | None = None  # "48201029"
