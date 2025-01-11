from fastapi import APIRouter


router = APIRouter(responses={404: {"description": "Not found"}})


@router.get(
    "/", response_model=str, summary="Проверка на рабочее состояние", description="Если нет ошибки, то сервис запущен"
)
async def health_check():
    return "Hello"