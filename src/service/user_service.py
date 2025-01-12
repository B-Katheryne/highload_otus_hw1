from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from uuid import UUID

import bcrypt
import jwt
from fastapi import HTTPException
from fastapi import status as status_code

from src.db.models.users import User
from src.repository.users import UserRepository
from src.schemas.users import AuthInfoIn, AuthInfoOut, RegistrationInfo
from src.utils.error_messages import LOGIN_TAKEN, WRONG_PASSWORD

SECRET_KEY = "very secret"  # noqa: S105
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class HTTPUserNotFoundException(HTTPException):
    def __init__(self, login: str | None = None):
        additional_text = f' с логином "{login}"' if login else ""
        detail = f"Пользователь{additional_text} не найден"
        super().__init__(status_code=status_code.HTTP_404_NOT_FOUND, detail=detail)


@dataclass
class UserService:
    user_repository: UserRepository

    async def get_user_profile_info_or_fail(self, id: UUID):
        if not (profile_info := await self.user_repository.get_user_profile_info(id=id)):
            raise HTTPUserNotFoundException

        return profile_info

    async def get_user_or_fail(self, login: str | None = None, id: UUID | None = None) -> User:
        if not (user := await self.user_repository.get(login=login, id=id)):
            raise HTTPUserNotFoundException(login=login)

        return user

    async def register(self, registration_info: RegistrationInfo):
        if user := await self.user_repository.get(login=registration_info.login):
            raise HTTPException(status_code=status_code.HTTP_400_BAD_REQUEST, detail=LOGIN_TAKEN)

        hashed_password = bcrypt.hashpw(registration_info.password.encode("utf-8"), bcrypt.gensalt())
        hashed_password_str = hashed_password.decode("utf-8")
        registration_info.password = hashed_password_str
        fields = registration_info.model_dump()
        user = await self.user_repository.add(fields)
        return user

    async def auth(self, auth_info: AuthInfoIn) -> AuthInfoOut:
        user = await self.get_user_or_fail(login=auth_info.login)

        if not bcrypt.checkpw(auth_info.password.encode("utf-8"), user.password.encode("utf-8")):
            raise HTTPException(status_code=status_code.HTTP_400_BAD_REQUEST, detail=WRONG_PASSWORD)

        token = self.create_access_token(data={"sub": str(user.id)})
        return AuthInfoOut(token=token, id=user.id)

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None) -> str:
        if expires_delta:
            expiration = datetime.now(tz=UTC) + expires_delta
        else:
            expiration = datetime.now(tz=UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode = data.copy()
        to_encode.update({"exp": expiration})

        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
