from src.dependency.infrastructure import DB
from src.repository.users import UserRepository


def get_user_repository(db: DB) -> UserRepository:
    return UserRepository(db=db)
