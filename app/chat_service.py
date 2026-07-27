from app.llm.groq_client import GroqClient
from app.rag.prompt_builder import build_rag_prompt
from app.rag.retriever import Retriever
from app.utils.citations import append_citations

class ChatService:
    def init(self):
        self.retriever = Retriever()
        self.llm = GroqClient()

    def ask(self, question:str) -> str:

        retrieved_chunks  =  self.retriever.retrieve(question)
        prompt = build_rag_prompt(
            question=question,
            retrieved_chunks=retrieved_chunks,
        )
        answer = append_citations(
            answer=answer,
            retrieved_chunks=retrieved_chunks,
        )
        return answer