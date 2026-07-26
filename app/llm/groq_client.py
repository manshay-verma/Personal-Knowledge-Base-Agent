from __future__ import annotations

import os

from groq import Groq


class GroqClient:
    def __init__(self, api_key: str | None = None, model: str | None = None) -> None:
        self.client = Groq(api_key=api_key or os.getenv("GROQ_API_KEY", ""))
        self.model = model or os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

    def chat(self, message: str) -> str:
        if not self.client.api_key:
            return f"Groq API key not configured. Received: {message}"
        return f"Groq response for: {message}"
