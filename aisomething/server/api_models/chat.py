from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    user_propmt: str = Field(alias="userPrompt")


class ChatResponse(BaseModel):
    chatbot_response_body: str = Field(alias="chatbotResponseBody")
    confidence_level: float = Field(alias="confidenceLevel")
