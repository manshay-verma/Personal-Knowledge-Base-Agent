from __future__ import annotations


def chunk_text(text: str, chunk_size: int = 500) -> list[str]:
    if not text.strip():
        return []

    words = text.split()
    return [" ".join(words[i : i + chunk_size]) for i in range(0, len(words), chunk_size)]
