from app.rag.embedder import Embedder
from app.rag.vectorstore import VectorStore

class LongTermMemory:
    def __init__(self):
        self.embedder = Embedder()
        self.vectorstore = VectorStore(
            collection_name="memory"
        )

    def store_memory(
            self,
            summary:str,
            metadata:dict | None = None
    )-> None:
        embedding = self.embedder.embed_documents([summary])
        meta = dict(metadata) if metadata else {}
        meta.setdefault("source", "conversation_memory")
        meta.setdefault("type","memory")

        self.vectorstore.add_documents(
            chunks=[summary],
            embedding=embedding,
            metadata=[meta],
        )

    def search_memory(
            self,
            query:str,
            k:int = 3,
    ):
        embedding = self.embedder.embed_query(query)
        return self.vectorstore.similarity_search(
            query_embedding= embedding,
            k=k,
        )

    def retrieve_memories(
            self,
            query:str,
            k:int = 3,
    ):
        query_embedding = self.embedder.embed_query(query)
        return self.vectorstore.similarity_search(
            query_embedding=query_embedding,
            k=k,
        )