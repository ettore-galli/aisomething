import os
from pathlib import Path

from aisomething.server.config.config import retrieve_config

CONFIG_ENV_FILE: Path = Path(__file__).parent / Path("data") / Path("config.env")


def test_retrieve_config() -> None:
    os.environ["DB_CONNECTION"] = "protocol://my-db-connection"
    os.environ["CONFIG_ENV_FILE"] = str(CONFIG_ENV_FILE)
    config = retrieve_config(env_file=str(CONFIG_ENV_FILE))

    assert config.db_connection_string == "protocol://my-db-connection"
    assert config.app_title == "My app"
