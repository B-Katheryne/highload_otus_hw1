from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base
from src.config import settings


db_url = settings.database_url
db_pool_size = settings.db_pool_size
db_max_overflow = settings.db_max_overflow

engine = create_async_engine(
    db_url, pool_size=db_pool_size, max_overflow=db_max_overflow
)
async_session = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()


async def get_session() -> AsyncGenerator[AsyncSession]:
    async with async_session() as session:
        yield session
