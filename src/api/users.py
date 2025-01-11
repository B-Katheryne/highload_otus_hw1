from uuid import UUID
from fastapi import APIRouter, status
from src.schemas.users import Token, UserProfileInfo, RegistrationInfo, AuthInfo
from src.dependency.service import UserServiceDependency

router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not found"}}
)


@router.post(
    "/register",
    response_model=UserProfileInfo,
    status_code=status.HTTP_201_CREATED,
    summary="Регистрация пользователя",
)
async def register(
    user_service: UserServiceDependency, registration_info: RegistrationInfo
):
    return await user_service.register(registration_info=registration_info)


@router.post("/login", response_model=Token, summary="Авторизация пользователя")
async def auth(user_service: UserServiceDependency, auth_info: AuthInfo):
    return await user_service.auth(auth_info=auth_info)


@router.get("/{id}/profle-info", response_model=UserProfileInfo)
async def get_proile_info(user_service: UserServiceDependency, id: UUID):
    return await user_service.get_user_profile_info_or_fail(id=id)
