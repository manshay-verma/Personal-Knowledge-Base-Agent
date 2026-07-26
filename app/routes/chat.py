from fastapi import APIRouter

from app.schemas import ChatRequest, ChatResponse

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    reply = f"Echo: {request.message}"
    return ChatResponse(reply=reply, sources=["uploaded-documents"])
