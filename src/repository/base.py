from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncConnection, AsyncSession
from src.db.base import Base


@dataclass
class BaseRepository:
    db: AsyncSession | AsyncConnection

    async def create(self, model_object: Base) -> Base:
        self.db.add(model_object)
        await self.db.flush()
        await self.db.commit()
        return model_object

    async def create_batch(self, model_objects: list[Base]):
        self.db.add_all(model_objects)
        await self.db.flush()
        await self.db.commit()
        return model_objects