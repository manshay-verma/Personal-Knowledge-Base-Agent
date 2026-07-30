from app.llm.groq_client import GroqClient
from app.memory.summarizer import ConversationSummarizer
from app.memory.long_term_memory import LongTermMemory
from app.rag.prompt_builder import build_rag_prompt
from app.rag.retriever import Retriever
from app.utils.citations import append_citations



class ChatService:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = GroqClient()
        self.memory = LongTermMemory()
        self.summarizer = ConversationSummarizer()

    def chat(self,question:str):
        retrieved_chunks = self.retriever.retrieve(question)

        prompt = build_rag_prompt(
            question=question,
            retrieved_chunks = retrieved_chunks
        )

        raw_answer = self.llm.generate(prompt)
        answer = append_citations(raw_answer,retrieved_chunks)

        return {
            "answer":answer,
            "sources":[
                chunk["metadata"].get("source","Unknown")
                for chunk in retrieved_chunks
            ],
        }

    def remember_conversation(self,conversation_text:str,conversation_id:int)->None:
        summary = self.summarizer.summarize(conversation_text)
        self.memory.store_memory(
            summary = summary,
            metadata={
                "source":f"conversation_{conversation_id}",
                "type":"memory",
            }
        )