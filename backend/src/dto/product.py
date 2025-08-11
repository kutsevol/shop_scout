from pydantic import BaseModel

from dto.discount import Discount
from dto.img import Img
from dto.nutrition_facts import NutritionFacts
from dto.producer import Producer
from dto.quantity import Quantity
from dto.restrictions import Restrictions


class Product(BaseModel):
    ean: str  # "04820000451888"
    sku: str  # "6195"
    title: str  # "Kvas Taras Bread Kvas 2l"
    price: int  # 6799
    price_wholesale: list  # []
    discount: Discount
    bundle: int  # 1
    unit: str  # "pcs"
    volume: int  # 2000
    quantity: Quantity
    currency: str  # "uah"
    category_id: str  # "kvass-pasteurized-novus"
    parent_category_id: str  # "drinks"
    category_filters: list  # []
    description: str  # "Highly carbonated pasteurized fermented drink. It has a refreshing sweet and sour taste with a touch of fresh rye bread. Available in several formats: PETF 0.5 l; 1l; 2l; 2.5l, keg 30l; 50l \nStore at temperatures from 0 ° C to 25 ° C. Light opalescence and sediment are allowed."
    nutrition_facts: NutritionFacts
    slug: str  # "kvas-kvas-taras-2000ml"
    in_stock: bool  # true
    is_hit: bool  # false
    is_alcohol: bool  # false
    is_nicotine: bool  # false
    is_ready_meal: bool  # false
    is_new_product: bool  # false
    horeca_only: bool  # true
    excisable: bool  # false
    web_url: str  # "https://novus.zakaz.ua/en/products/kvas-kvas-taras-2000ml--04820000451888/"
    restrictions: Restrictions
    ingredients: list[
        str
    ]  # ["Drinking water, glucose-fructose syrup, barley, rye malt, barley malt, concentrate of leavened wort (rye flour, rye malt, barley malt), yeast, citric acid acidity regulator.\u003Cbr\u003E"]
    fat: str  # null
    shelf_life: str  # "180 days"
    temperature_range: str  # "0...25"
    pack_amount: str  # null
    country: str  # "Ukraine"
    producer: Producer
    custom_ribbons: list  # []
    img: Img
    gallery: list[dict]  # [{
    #    "s150x150": "https://img3.zakaz.ua/5b365cbefa4846ef9ea45bdbfc3a1fef/1754296399-s150x150.jpg",
    #    "s200x200": "https://img3.zakaz.ua/5b365cbefa4846ef9ea45bdbfc3a1fef/1754296399-s200x200.jpg",
    #    "s350x350": "https://img3.zakaz.ua/5b365cbefa4846ef9ea45bdbfc3a1fef/1754296399-s350x350.jpg",
    #    "s1350x1350": "https://img2.zakaz.ua/5b365cbefa4846ef9ea45bdbfc3a1fef/1754296399-s1350x1350.jpg"
    # }]
    is_uber_item: bool  # false
    verbose_stock: str  # "low_stock"
    take_more: bool  # false
    is_own_brand: bool  # false
    available_for_cart: bool  # true
    own_brand_data: dict  # {}
    taxons: list  # []
    weight: str  # null
    has_similar_products: str  # null
    hits: int  # 2
    shopping_list_count: str  # null
    store_id: str  # "48201029"
