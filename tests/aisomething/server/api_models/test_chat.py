from aisomething.server.api_models.chat import ChatResponse


def test_chat() -> None:
    assert ChatResponse(
        chatbot_response_body="Hello", confidence_level=0.9876
    ).model_dump() == {
        "chatbot_response_body": "Hello",
        "confidence_level": 0.9876,
    }
