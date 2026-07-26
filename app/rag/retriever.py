from __future__ import annotations

from app.rag.embedder import Embedder
from app.rag.vectorstore import VectorStore


class Retriever:
    def __init__(self, vectorstore: VectorStore | None = None) -> None:
        self.vectorstore = vectorstore or VectorStore()
        self.embedder = Embedder()

    def retrieve(self, query: str, top_k: int = 3) -> list[dict[str, object]]:
        query_embedding = self.embedder.embed(query)
        result = self.vectorstore.collection.query(query_embeddings=[query_embedding], n_results=top_k)
        return [
            {"text": text, "metadata": metadata}
            for text, metadata in zip(result.get("documents", [[]])[0], result.get("metadatas", [[]])[0], strict=False)
        ]
