from fastapi import APIRouter, Depends, HTTPException

from app.schemas import ChatRequest, ChatResponse, MessageResponse, ConversationResponse
from app.chat_service import ChatService

from sqlalchemy.orm import Session
from app.db.database import get_db 
from app.db.models import Conversation, Message


router = APIRouter(prefix="/chat", tags=["chat"])


chat_service = ChatService()

@router.post("/",response_model=ChatResponse)
def chat(request: ChatRequest, db:Session = Depends(get_db)):
    if request.conversation_id:
        conversation = (
            db.query(Conversation)
            .filter(Conversation.id == request.conversation_id)
            .first()
        )
        if conversation is None:
            raise HTTPException(
                status_code= 404,
                 detail= "Conversation not found"
            )
    else:
        conversation = Conversation(title=request.message[:50])
        db.add(conversation)
        db.commit()
        db.refresh(conversation)

    db.add(Message(role='user', content=request.message, conversation_id=conversation.id))
    db.commit()

    result = chat_service.chat(request.message)
    db.add(Message(role='user',content=request.message, conversation_id=conversation.id))
    db.commit()

    return ChatResponse(
        reply = result["answer"],
        conversation_id=conversation.id,
        sources=result['sources']
    )

@router.get("/{conversation_id}", response_model=ConversationResponse)
def get_conversation(
    conversation_id:int,
    db:Session = Depends(get_db)
):
    conversation = (
        db.query(Conversation)
        .filter(Conversation.id == conversation_id)
        .first()
    )

    if conversation is None:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )

    return conversation