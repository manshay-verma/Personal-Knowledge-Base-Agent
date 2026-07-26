from __future__ import annotations

from app.rag.embedder import Embedder
from app.rag.vectorstore import VectorStore


class Retriever:
    def __init__(
            self,
            embedder:Embedder | None = None,
            vectorstore:VectorStore | None = None
    ):
        self.embedder = embedder or Embedder()
        self.vectorstore = vectorstore or VectorStore()

    def retrieve(
            self,
            query: str,
            k: int = 5,
    ) -> list[dict]:
        """
        Retrieve top-k similar chunks.

        Returns:
            [
                {
                    "text": "...",
                    "metadata": {...},
                    "distance": 0.12
                },
                ...
            ]
        """
        query_embedding = self.embedder.embed_query(query)
        results = self.vectorstore.similarity_search(
            query_embedding=query_embedding,
            k=k
        )
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        retrieved = []

        for doc, meta, distance in zip(
            documents,
            metadatas,
            distances,
        ):
            retrieved.append(
                {
                    "text":doc,
                    "metadata":meta,
                    "distance":distance,
                }
            )
        return retrieved
