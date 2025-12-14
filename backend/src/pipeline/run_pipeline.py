import asyncio
import logging

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel

from core.config import settings
from pipeline.extractor.extractor import extract_data
from pipeline.loader.loader import DataLoader
from pipeline.transform.transform import transform_data


async def create_tables() -> None:
    engine = create_async_engine(settings.database_url, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    await engine.dispose()


async def run_pipeline(store_id: str) -> None:
    logging.basicConfig(level=logging.INFO)

    # 1. EXTRACT
    logging.info("Extracting data...")
    products = await extract_data(store_id)
    logging.info(f"Extracted {len(products)} raw products.")

    # 2. TRANSFORM
    logging.info("Transforming data...")
    transformed = transform_data(products)

    # !!! associations for link table
    transformed["links"] = [
        {"ean": p["ean"], "store_id": p["store_id"], "category_id": p["category_id"]}
        for p in transformed["products"]
    ]

    # 3. LOAD
    loader = DataLoader(settings.database_url, echo=settings.db_echo)

    logging.info("Loading into database...")
    await loader.load(transformed)

    logging.info("Pipeline completed successfully!")


if __name__ == "__main__":
    asyncio.run(create_tables())
    asyncio.run(run_pipeline(store_id="48215633"))
