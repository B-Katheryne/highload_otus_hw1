from dataclasses import dataclass

from sqlalchemy import UUID

from src.repository.users import UserRepository


@dataclass
class UserService:
    user_repository: UserRepository

    async def get_user_profile_info_or_fail(self, id: UUID):
        return await self.user_repository.get_user_profile_info(id=id)

    async def register(self, registration_info):
        pass

    async def auth(self, auth_info):
        pass
