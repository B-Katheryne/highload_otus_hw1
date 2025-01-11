from datetime import date
from uuid import UUID

from pydantic import BaseModel


class Token(BaseModel):
    token: str


class UserId(BaseModel):
    id: UUID


class UserPassword(BaseModel):
    password: str


class UserProfileInfo(BaseModel):
    second_name: str
    first_name: str
    city: str | None
    biography: str | None
    birthdate: date | None


class RegistrationInfo(UserPassword):
    second_name: str
    first_name: str
    city: str | None = None
    biography: str | None = None
    birthdate: date | None = None


class AuthInfo(UserId, UserPassword):
    pass
