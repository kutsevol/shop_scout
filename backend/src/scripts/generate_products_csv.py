import httpx
import polars as pl

from core.config import AppSettings
from dto.product import Product

settings = AppSettings()

BASE_URL = settings.zakaz_api_base_url

store_id = "482010105"  # NOVUS

queries = [
    "bread",
    "fruits",
    "vegetables",
    "berries",
    "nuts",
    "cheese",
    "chicken",
    "milk",
    "yogurt",
    "butter",
    "eggs",
    "meat",
    "sausages",
    "fish",
]

all_products = []
for query in queries:
    page = 1
    while True:
        params: dict[str, str | int] = {"q": query, "page": page}

        r = httpx.get(
            f"{BASE_URL}/stores/{store_id}/products/search/",
            params=params,
            follow_redirects=True,
            timeout=120,
        )

        r.raise_for_status()
        data = r.json()
        if not data.get("results"):
            break

        all_products.extend(data["results"])
        page += 1

products = [Product(**product) for product in all_products]

df = pl.DataFrame(products, infer_schema_length=500).select(
    ["ean", "title", "price", "category_id", "parent_category_id", "country", "store_id"]
)
df = df.with_columns(pl.lit(f"{store_id}").alias("store_id"))
df.write_csv("products.csv")
print(f"Saved {len(df)} products")
