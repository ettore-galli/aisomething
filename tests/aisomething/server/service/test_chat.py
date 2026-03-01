from aisomething.server.config.config import ServerConfig
from aisomething.server.service.chat import (
    ChatServiceRequest,
    ChatServiceResponse,
    process_chat_prompt,
)


def test_process_chat_prompt(server_config: ServerConfig) -> None:
    assert process_chat_prompt(
        config=server_config, chat_request=ChatServiceRequest(user_propmt="who am I?")
    ) == ChatServiceResponse(
        chatbot_response_body="Hello, who am I?!", confidence_level=1
    )
