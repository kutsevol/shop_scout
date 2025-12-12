from decimal import Decimal
from typing import List

from sqlmodel import Field, Relationship, SQLModel


# ──────────────── Category ────────────────
class Category(SQLModel, table=True):
    __tablename__ = "categories"

    id: str = Field(primary_key=True)
    store_id: str

    product_links: List["ProductCategoryLink"] = Relationship(back_populates="category")


# ──────────────── Product ────────────────
class Product(SQLModel, table=True):
    __tablename__ = "products"

    ean: str = Field(primary_key=True)
    store_id: str
    title: str
    producer: str | None

    category_links: List["ProductCategoryLink"] = Relationship(back_populates="product")
    prices: List["ProductPrice"] = Relationship(back_populates="product")


# ──────────────── Link Table ────────────────
class ProductCategoryLink(SQLModel, table=True):
    __tablename__ = "product_categories"

    ean: str = Field(foreign_key="products.ean", primary_key=True)
    category_id: str = Field(foreign_key="categories.id", primary_key=True)
    store_id: str
    category_store_id: str | None

    product: Product = Relationship(back_populates="category_links")
    category: Category = Relationship(back_populates="product_links")


# ──────────────── Product Price ────────────────
class ProductPrice(SQLModel, table=True):
    __tablename__ = "product_prices"

    ean: str = Field(foreign_key="products.ean", primary_key=True)
    store_id: str = Field(primary_key=True)
    price: Decimal = Field(sa_column_kwargs={"nullable": False})

    product: Product = Relationship(back_populates="prices")
