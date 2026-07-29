from fastapi import APIRouter

from app.schemas import ChatRequest, ChatResponse
from app.chat_service import ChatService

router = APIRouter(prefix="/chat", tags=["chat"])


chat_service = ChatService()

@router.post("/",response_model=ChatResponse)
def chat(request: ChatRequest):
    result = chat_service.chat(request.message) 

    return ChatResponse(
        reply = result["answer"],
        conversation_id=request.conversation_id,
        sources=result['sources']
    )