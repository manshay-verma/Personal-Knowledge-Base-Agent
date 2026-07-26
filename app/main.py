from fastapi import FastAPI

from app.routes import chat, documents
from app.config import settings

app = FastAPI(title="Personal KB Agent", version="0.1.0")
app.include_router(documents.router)
app.include_router(chat.router)


@app.get("/check")
async def root() -> dict[str, str]:
    return {"message": f"{settings.app_name} is running"}

