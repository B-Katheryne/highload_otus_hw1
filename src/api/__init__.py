from src.api.users import router as users_router

# Обязательно давать алиас router-у, который заканчивается на _router
routers = [
    value
    for name, value in globals().items()
    if name.endswith("_router") and callable(value)
]
