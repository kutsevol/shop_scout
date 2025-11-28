from sqlalchemy import ForeignKeyConstraint, Index, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from pipeline.transform.transform import (
    CategoryEntity,
    ProductEntity,
    ProductPriceEntity,
    TransformResult,
)


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    store_id: Mapped[str] = mapped_column(String, primary_key=True)

    __table_args__ = (Index("idx_categories_store", "store_id"),)


class Product(Base):
    __tablename__ = "products"

    ean: Mapped[str] = mapped_column(String, primary_key=True)
    store_id: Mapped[str] = mapped_column(String, primary_key=True)
    title: Mapped[str] = mapped_column(String)

    category_id: Mapped[str] = mapped_column(String)

    producer: Mapped[str | None] = mapped_column(String, nullable=True)
    categories: Mapped[str] = mapped_column(String)

    __table_args__ = (
        ForeignKeyConstraint(
            ["category_id", "store_id"],
            ["categories.id", "categories.store_id"],
            ondelete="RESTRICT",
        ),
        Index("idx_products_title", "title"),
        Index("idx_products_category", "category_id"),
    )


class ProductPrice(Base):
    __tablename__ = "prises"

    ean: Mapped[str] = mapped_column(String, primary_key=True)
    store_id: Mapped[str] = mapped_column(String, primary_key=True)
    price: Mapped[str] = mapped_column(Integer)

    __table_args__ = (
        Index("idx_prises_store", "store_id"),
        Index("idx_prises_price", "price"),
    )


class DataLoader:
    def __init__(self, dsn: str) -> None:
        self.engine = create_async_engine(dsn, echo=False)
        self.Session = async_sessionmaker(self.engine, expire_on_commit=False)

    async def migrate(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def load_categories(self, session: AsyncSession, categories: list[CategoryEntity]):
        objs = [Category(**c) for c in categories]
        session.add_all(objs)

    async def load_products(self, session: AsyncSession, products: list[ProductEntity]):
        objs = [Product(**p) for p in products]
        session.add_all(objs)

    async def load_prices(self, session: AsyncSession, prices: list[ProductPriceEntity]):
        objs = [ProductPrice(**p) for p in prices]
        session.add_all(objs)

    async def load(self, transformed_data: TransformResult):
        async with self.Session() as session:
            async with session.begin():
                await self.load_categories(session, transformed_data.get("categories") or [])
                await self.load_products(session, transformed_data.get("products") or [])
                await self.load_prices(session, transformed_data.get("prices") or [])
