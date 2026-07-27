from langchain_groq import ChatGroq
from app.config import settings

class ConversationSummarizer:
    def __init__(self):
        self.llm = ChatGroq(
            groq_api_key = settings.groq_api_key,
            model= settings.groq_model,
            temperature=0.2
        )

    def summarize(
            self,
            conversation:str
    )->str:
        
        prompt = f"""
You are an AI assistant.

Summarize the following conversation in 2-3 sentences.

Focus on:

- User goals
- Important facts
- Preferences
- Decisions

Conversation:

{conversation}

Summary:
"""
        response = self.llm.invoke(prompt)
        return response.content.strip()
