import pytest
from aisomething.server.config.config import DatabaseConfig, GeneralConfig, ServerConfig


@pytest.fixture
def server_config() -> ServerConfig:
    return ServerConfig(
        general=GeneralConfig(app_title="Title", app_description="Descr"),
        database=DatabaseConfig(db_connection_string="my test connection string"),
    )
