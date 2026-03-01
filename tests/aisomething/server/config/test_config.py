import os
from pathlib import Path

from aisomething.server.config.config import retrieve_config

ENV_FILE: Path = Path(__file__).parent / Path("data") / Path("config.env")


def test_retrieve_config() -> None:
    os.environ["EG_DATABASE__DB_CONNECTION_STRING"] = "protocol://my-db-connection"
    os.environ["EG_ENV_FILE"] = str(ENV_FILE)
    config = retrieve_config(env_prefix="EG_")

    assert config.database.db_connection_string == "protocol://my-db-connection"
    assert config.general.app_title == "My app"
    assert config.general.app_description == "My wonderful app"
