from pathlib import Path
from typing import Any
import uuid

import chromadb
from chromadb.api.models.Collection import Collection

class VectorStore:
    def __init__(
            self,
            persist_directory:str = "data/chroma",
            collection_name:str="personal_kb"
            ):
        Path(persist_directory).mkdir(parents=True, exist_ok=True)
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection:Collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_documents(
            self,
            chunks:list[str],
            embedding:list[list[float]],
            metadata:list[dict[str,Any]] | None = None
    )->None:
        if metadata is None:
            metadata = [{} for _ in chunks]

        ids = [
            f"{uuid.uuid4()}"
            for _ in chunks
            ]
        self.collection.add(
            ids = ids,
            documents=chunks,
            embeddings=embedding,
            metadatas=metadata,
        )

    def similarity_search(
        self,
        query_embedding:list[float],
        k:int=3
    )->dict:
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )

    def reset(self)->int:
        self.client.delete_collection(self.collection.name)
        self.collection = self.client.get_or_create_collection(
            self.collection.name
        )

    def count(self)-> int:
        return self.collection.count()
        