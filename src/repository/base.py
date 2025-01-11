from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncConnection, AsyncSession


@dataclass
class BaseRepository:
    db: AsyncSession | AsyncConnection
