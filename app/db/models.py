from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100),unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    documents = relationship("Document",back_populates="user")
    conversations = relationship("Conversation", back_populates="user")

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index = True)
    filename = Column(String(255), nullable=False)
    filepath = Column(String(500), nullable=False)
    uploaded_at = Column(DateTime, default=datetime.now)

    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="documents")

class Conversation(Base):
    __tablename__="conversations"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    started_at = Column(DateTime, default=datetime.now)

    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="conversations")
    message = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete-orphan",
    )

class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(20), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    conversation_id = Column(
        Integer,
        ForeignKey("coversations.id"),
    )
    conversation = relationship(
        "Conversation",
        back_populates="messages",
    )