from aisomething.server.config.config import ServerConfig, retrieve_config

ENV_PREFIX = "EG_"


def retrieve_server_configuration() -> ServerConfig:
    return retrieve_config(env_prefix=ENV_PREFIX)
