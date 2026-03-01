export PYTHONPATH=.
# Use module:callable syntax so the CLI imports the FastAPI `app` variable
# (replace with `uvicorn aisomething.server.main:app --reload` if preferred)
uvicorn aisomething.server.main:app --reload