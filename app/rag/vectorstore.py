from __future__ import annotations

import os
from typing import Any

import chromadb
from chromadb.config import Settings as ChromaSettings


class VectorStore:
    def __init__(self, persist_dir: str | None = None) -> None:
        self.persist_dir = persist_dir or os.getenv("CHROMA_PERSIST_DIR", "data/chroma_db")
        self.client = chromadb.PersistentClient(path=self.persist_dir, settings=ChromaSettings(allow_reset=True))
        self.collection = self.client.get_or_create_collection(name="documents")

    def add_documents(self, documents: list[dict[str, Any]]) -> None:
        if not documents:
            return
        self.collection.add(
            documents=[doc["text"] for doc in documents],
            metadatas=[doc.get("metadata", {}) for doc in documents],
            ids=[doc["id"] for doc in documents],
        )

    def query(self, query_text: str, n_results: int = 3) -> Any:
        return self.collection.query(query_texts=[query_text], n_results=n_results)
