from pydantic import BaseModel, Field
from datetime import datetime


class DocumentUploadRequest(BaseModel):
    filename: str = Field(..., min_length=1)


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)
    conversation_id:int | None = None
    history: list[tuple[str, str]] | None = None


class ChatResponse(BaseModel):
    reply: str
    conversation_id:int | None = None
    sources: list[str] = []

class MessageResponse(BaseModel):
    id:int
    role:str
    content:str
    created_at:datetime
    model_config={
        "from_attributes":True
    }

class ConversationResponse(BaseModel):
    id:int
    title:str | None=None
    created_at:datetime
    messages:list[MessageResponse]
    model_config = {
        "from_attributes":True
    }