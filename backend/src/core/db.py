import asyncio

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlmodel import SQLModel

DATABASE_URL = "postgresql+asyncpg://oleksandra:@localhost:5432/shop_scout"

engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True)


async def reset_db() -> None:
    async with engine.begin() as conn:
        # видалити всі таблиці
        await conn.run_sync(SQLModel.metadata.drop_all)
        # створити всі таблиці заново
        await conn.run_sync(SQLModel.metadata.create_all)


asyncio.run(reset_db())
