from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "personal-kb-agent")
    groq_api_key: str | None = os.getenv("GROQ_API_KEY")
    groq_model: str = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
    chroma_persist_dir: str = os.getenv("CHROMA_PERSIST_DIR", "data/chroma_db")
    upload_dir: str = os.getenv("UPLOAD_DIR", "data/uploads")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///data/personal_kb_agent.db")


settings = Settings()
