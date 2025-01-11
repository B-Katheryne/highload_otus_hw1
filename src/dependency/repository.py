from src.repository.users import UserRepository
from src.dependency.infrastructure import DB


def get_user_repository(db: DB) -> UserRepository:
    return UserRepository(db=db)
