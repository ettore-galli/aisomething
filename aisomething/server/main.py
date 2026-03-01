from fastapi import FastAPI

from aisomething.server.controllers.chat import router as chat_router

app = FastAPI()

app.include_router(chat_router)


@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}
