from __future__ import annotations

from typing import Any, Dict, List, Mapping

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlmodel import SQLModel

from dto.models import Category, Product, ProductCategoryLink, ProductPrice


class DataLoader:
    def __init__(self, dsn: str, echo: bool = False) -> None:
        self.engine = create_async_engine(dsn, echo=echo, future=True)
        self.Session = async_sessionmaker(self.engine, expire_on_commit=False, autoflush=False)

    async def migrate(self) -> None:
        """Dev-only — creates tables. Production uses Alembic."""
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    async def _bulk_upsert(
        self,
        session: AsyncSession,
        table: type[SQLModel],
        rows: List[Dict],
        conflict_col: str | List[str],
    ) -> None:
        if not rows:
            return

        if isinstance(conflict_col, str):
            conflict_col = [conflict_col]

        model_columns = set(table.model_fields.keys())

        BATCH_SIZE = 500
        for i in range(0, len(rows), BATCH_SIZE):
            batch = rows[i : i + BATCH_SIZE]

            cleaned_batch = [{k: v for k, v in row.items() if k in model_columns} for row in batch]
            if not cleaned_batch:
                continue

            stmt = insert(table).values(cleaned_batch)

            update_cols = {
                col: stmt.excluded[col]
                for col in cleaned_batch[0].keys()
                if col not in conflict_col
            }

            if update_cols:
                stmt = stmt.on_conflict_do_update(
                    index_elements=conflict_col,
                    set_=update_cols,
                )
            else:
                stmt = stmt.on_conflict_do_nothing(index_elements=conflict_col)

            await session.execute(stmt)

    # ---- UPSERT methods ----

    async def upsert_categories(self, session: AsyncSession, categories: List[Dict]) -> None:
        await self._bulk_upsert(session, Category, categories, conflict_col="id")

    async def upsert_products(self, session: AsyncSession, products: List[Dict]) -> None:
        await self._bulk_upsert(session, Product, products, conflict_col="ean")

    async def upsert_prices(self, session: AsyncSession, prices: List[Dict]) -> None:
        # composite PK = (ean, store_id)
        await self._bulk_upsert(
            session,
            ProductPrice,
            prices,
            conflict_col=["ean", "store_id"],
        )

    async def upsert_product_category_links(self, session: AsyncSession, links: List[Dict]) -> None:
        # composite PK = (ean, category_id)
        await self._bulk_upsert(
            session,
            ProductCategoryLink,
            links,
            conflict_col=["ean", "category_id"],
        )

    # ---- Main loader ----
    async def load(self, data: Mapping[str, Any]) -> None:
        """Load everything in a single transaction (atomic)."""
        async with self.Session() as session:
            async with session.begin():
                await self.upsert_categories(session, data.get("categories", []))
                await self.upsert_products(session, data.get("products", []))
                await self.upsert_prices(session, data.get("prices", []))
                await self.upsert_product_category_links(session, data.get("links", []))
