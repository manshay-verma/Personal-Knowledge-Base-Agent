from langchain_groq import ChatGroq
from app.config import settings

class GroqClient:
    def __init__(self):
        self.llm = ChatGroq(
            groq_api_key=settings.groq_api_key,
            model=settings.groq_model,
            temperature=0.2,
        )

    def generate(self, prompt:str)->str:
        response = self.llm.invoke(prompt)
        return response.content