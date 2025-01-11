from typing import Annotated

from fastapi import Depends
from src.dependency.repository import get_user_repository
from src.repository.users import UserRepository
from src.service.user_service import UserService


def get_user_service(
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
) -> UserService:
    return UserService(user_repository=user_repository)


UserServiceDependency = Annotated[UserService, Depends(get_user_service)]
