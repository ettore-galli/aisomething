import pytest
from aisomething.server.config.config import ServerConfig

from tests.aisomething.tests_base import TESTS_SERVER_CONFIG


@pytest.fixture
def server_config() -> ServerConfig:
    return TESTS_SERVER_CONFIG
