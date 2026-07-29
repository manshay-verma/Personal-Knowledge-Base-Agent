from pydantic import BaseModel, Field


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
