from sqlalchemy import UUID, RowMapping, select
from src.db.models.users import User
from src.repository.base import BaseRepository


class UserRepository(BaseRepository):

    async def get_user_profile_info(self, id: UUID) -> RowMapping:
        query = select(
            User.first_name, User.second_name, User.city, User.birthdate, User.biography
        ).where(User.id == id)
        return (await self.db.execute(query)).mappings().one_or_none()

    async def get(self, *, login: str | None = None, id: UUID | None = None) -> User | None:
        query = select(User)
        if login:
            query = query.filter(User.login == login)
        elif id:
            query = query.filter(User.id == id)
        else:
            raise ValueError
        return (await self.db.execute(query)).scalar_one_or_none()

    async def add(self, fields: dict) -> User:
        return await self.create(User(**fields))