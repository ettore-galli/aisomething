from fastapi import APIRouter

from aisomething.server.api_models.chat import ChatRequest, ChatResponse
from aisomething.server.service.chat import ChatServiceRequest, process_chat_prompt

router = APIRouter(prefix="/chatbot", tags=["users"])


@router.post("/")
def respond_to_user(request: ChatRequest) -> ChatResponse:
    response = process_chat_prompt(
        chat_request=ChatServiceRequest(user_propmt=request.user_propmt)
    )
    return ChatResponse(
        chatbotResponseBody=response.chatbot_response_body,
        confidenceLevel=response.confidence_level,
    )
