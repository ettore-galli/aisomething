from aisomething.server.config.config import DatabaseConfig, GeneralConfig, ServerConfig

TESTS_SERVER_CONFIG = ServerConfig(
    general=GeneralConfig(app_title="Title", app_description="Descr"),
    database=DatabaseConfig(db_connection_string="my test connection string"),
)
