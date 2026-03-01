from aisomething.server.service.chat import (
    ChatServiceRequest,
    ChatServiceResponse,
    process_chat_prompt,
)


def test_process_chat_prompt() -> None:
    assert process_chat_prompt(
        chat_request=ChatServiceRequest(user_propmt="who am I?")
    ) == ChatServiceResponse(
        chatbot_response_body="Hello, who am I?!", confidence_level=1
    )
