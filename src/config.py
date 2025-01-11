from json import dumps

import structlog
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi_offline import FastAPIOffline
from starlette.middleware.cors import CORSMiddleware

from src.settings import Settings

settings = Settings(_env_file=".env")


def non_ascii_dumps(obj, **kwargs):
    return dumps(obj, ensure_ascii=False, **kwargs)


structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.format_exc_info,
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer(serializer=non_ascii_dumps),
    ],
    cache_logger_on_first_use=True,
)
log = structlog.get_logger()


app = FastAPIOffline(debug=settings.app_debug)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    expose_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc) -> JSONResponse:
    await log.aerror(
        "Ошибка валидации",
        error=repr(exc.errors()),
        body=exc.body,
        path_params=request.path_params,
        query_params=request.query_params,
    )
    return await request_validation_exception_handler(request, exc)
