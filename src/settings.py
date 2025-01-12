from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_debug: bool = Field(validation_alias="APP_DEBUG", default=False)

    database_url: str = Field(validation_alias="DATABASE_URL")
    db_pool_size: int = Field(validation_alias="DB_POOL_SIZE")
    db_max_overflow: int = Field(validation_alias="DB_MAX_OVERFLOW")

    salt: str = Field(validation_alias="SALT")

    model_config = SettingsConfigDict(env_file="../.env", extra="allow")
