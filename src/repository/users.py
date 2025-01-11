from sqlalchemy import UUID, RowMapping, select
from src.db.models.users import User
from src.repository.base import BaseRepository


class UserRepository(BaseRepository):

    async def get_user_profile_info(self, id: UUID) -> RowMapping:
        query = select(
            User.first_name, User.second_name, User.city, User.birthdate, User.biography
        ).where(User.id == id)
        return (await self.db.execute(query)).mappings().one_or_none()
