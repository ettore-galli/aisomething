export PYTHONPATH=.

export EG_DATABASE__DB_CONNECTION_STRING="protocol://my-db-connection"
export EG_ENV_FILE="local/etc/local.config.env"

# Use module:callable syntax so the CLI imports the FastAPI `app` variable
# (replace with `uvicorn aisomething.server.main:app --reload` if preferred)
uvicorn aisomething.server.main:app --reload