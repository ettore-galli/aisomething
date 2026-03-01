from pydantic import BaseModel, Field


class CustomModel(BaseModel):
    model_config = {
        "populate_by_name": True,
    }


class ChatRequest(CustomModel):
    user_propmt: str = Field(alias="userPrompt")


class ChatResponse(CustomModel):
    chatbot_response_body: str = Field(alias="chatbotResponseBody")
    confidence_level: float = Field(alias="confidenceLevel")
