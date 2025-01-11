from dataclasses import dataclass
from uuid import UUID
import bcrypt
import jwt
from datetime import UTC, datetime, timedelta
from src.repository.users import UserRepository
from src.schemas.users import AuthInfo, RegistrationInfo, Token

SECRET_KEY = "very secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


@dataclass
class UserService:
    user_repository: UserRepository

    async def get_user_profile_info_or_fail(self, id: UUID):
        return await self.user_repository.get_user_profile_info(id=id)


    async def register(self, registration_info: RegistrationInfo):
        hashed_password = bcrypt.hashpw(registration_info.password.encode('utf-8'), bcrypt.gensalt())
        registration_info.password = hashed_password
        fields = registration_info.model_dump() 
        user = await self.user_repository.add(fields)
        return user

    async def auth(self, auth_info: AuthInfo) -> Token:
        user = await self.user_repository.get(login=auth_info.login)
        
        if not user:
            raise Exception("Invalid credentials")

        if not bcrypt.checkpw(auth_info.password.encode('utf-8'), user.password.encode('utf-8')):
            raise Exception("Invalid credentials")
        
        token = self.create_access_token(data={"sub": str(user.id)})
        return Token(token=token)

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None) -> str:
        if expires_delta:
            expiration = datetime.now(tz=UTC) + expires_delta
        else:
            expiration = datetime.now(tz=UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
        to_encode = data.copy()
        to_encode.update({"exp": expiration})
        
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
