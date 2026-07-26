from pydantic import BaseModel, Field


class DocumentUploadRequest(BaseModel):
    filename: str = Field(..., min_length=1)


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)
    history: list[tuple[str, str]] | None = None


class ChatResponse(BaseModel):
    reply: str
    sources: list[str] = []
