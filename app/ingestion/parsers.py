from __future__ import annotations

from pathlib import Path


def extract_text(file_path: str | Path) -> str:
    path = Path(file_path)
    if path.suffix.lower() == ".md":
        return path.read_text(encoding="utf-8")
    if path.suffix.lower() in {".txt", ".rst"}:
        return path.read_text(encoding="utf-8")
    return f"Unsupported file type: {path.suffix}"
