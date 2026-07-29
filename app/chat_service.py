from app.llm.groq_client import GroqClient
from app.rag.prompt_builder import build_rag_prompt
from app.rag.retriever import Retriever
from app.utils.citations import append_citations


class ChatService:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = GroqClient()

    def chat(self,question:str):
        retrieved_chunks = self.retriever.retrieve(question)

        prompt = build_rag_prompt(
            question=question,
            retrieved_chunks = retrieved_chunks
        )

        answer = self.llm.generate(prompt)
        print("=" * 50)
        print("=" * 50)
        print(f"Retrieved Chunks: {len(retrieved_chunks)}")
        print(f"Prompt Length (chars): {len(prompt)}")
        print(prompt)
        print("=" * 50)

        return {
            "answer":answer,
            "sources":[
                chunk["metadata"].get("source","Unknown")
                for chunk in retrieved_chunks
            ],
        }