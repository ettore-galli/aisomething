from dataclasses import dataclass

from aisomething.server.config.config import ServerConfig


@dataclass
class ChatServiceRequest:
    user_propmt: str


@dataclass
class ChatServiceResponse:
    chatbot_response_body: str
    confidence_level: float


def process_chat_prompt(
    config: ServerConfig, chat_request: ChatServiceRequest
) -> ChatServiceResponse:
    _ = config
    return ChatServiceResponse(
        chatbot_response_body=f"Hello, {chat_request.user_propmt}!",
        confidence_level=1.0,
    )
