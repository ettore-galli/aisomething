import os
from typing import ClassVar

from pydantic import Field
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class TemplateConfig(BaseSettings):
    ENV_FILE_ENVVAR_NAME: ClassVar[str] = "ENV_FILE"
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_nested_delimiter="__",
    )


class GeneralConfig(TemplateConfig):
    app_title: str = Field()
    app_description: str = Field()


class DatabaseConfig(TemplateConfig):
    db_connection_string: str = Field()


class ServerConfig(TemplateConfig):
    general: GeneralConfig = Field()
    database: DatabaseConfig = Field()


def retrieve_config(env_prefix: str | None = None) -> ServerConfig:
    prefix = env_prefix or ""
    env_file = os.environ.get(f"{prefix}{ServerConfig.ENV_FILE_ENVVAR_NAME}")
    return ServerConfig(_env_prefix=prefix, _env_file=env_file)  # type: ignore[call-arg]
