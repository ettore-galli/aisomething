import os

from pydantic import Field
from pydantic_settings import (
    BaseSettings,
    DotEnvSettingsSource,
    PydanticBaseSettingsSource,
)


class ServerConfig(BaseSettings):
    app_title: str = Field(alias="APP_TITLE")
    db_connection_string: str = Field(alias="DB_CONNECTION")

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        _ = settings_cls, dotenv_settings

        custom_dotenv = DotEnvSettingsSource(
            settings_cls, env_file=os.environ.get("CONFIG_ENV_FILE", ".env")
        )

        return (
            init_settings,
            env_settings,
            custom_dotenv,
            file_secret_settings,
        )


def retrieve_config(env_file: str | None = None) -> ServerConfig:
    if env_file:
        os.environ["CONFIG_ENV_FILE"] = env_file
    return ServerConfig()  # type: ignore[call-arg]
