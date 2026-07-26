from __future__ import annotations

from app.rag.embedder import Embedder


class LongTermMemory:
    def __init__(self) -> None:
        self.embedder = Embedder()

    def remember(self, text: str) -> list[float]:
        return self.embedder.embed(text)
