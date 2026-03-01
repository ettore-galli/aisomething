from typing import Annotated

from fastapi import APIRouter, Depends

from aisomething.server.api_models.chat import ChatRequest, ChatResponse
from aisomething.server.base import retrieve_server_configuration
from aisomething.server.config.config import ServerConfig
from aisomething.server.service.chat import ChatServiceRequest, process_chat_prompt

router = APIRouter(prefix="/chatbot", tags=["users"])


@router.post("/")
def respond_to_user(
    request: ChatRequest,
    config: Annotated[ServerConfig, Depends(retrieve_server_configuration)],
) -> ChatResponse:
    response = process_chat_prompt(
        config=config, chat_request=ChatServiceRequest(user_propmt=request.user_propmt)
    )
    return ChatResponse(
        chatbot_response_body=response.chatbot_response_body,
        confidence_level=response.confidence_level,
    )
