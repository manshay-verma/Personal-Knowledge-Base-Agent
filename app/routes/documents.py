from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.config import settings

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)) -> dict[str, str]:
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is required")

    upload_dir = Path(settings.upload_dir)
    upload_dir.mkdir(parents=True, exist_ok=True)

    destination = upload_dir / file.filename
    content = await file.read()
    destination.write_bytes(content)

    return {"message": "Document uploaded", "filename": file.filename}


@router.get("")
async def list_documents() -> dict[str, list[str]]:
    upload_dir = Path(settings.upload_dir)
    if not upload_dir.exists():
        return {"documents": []}

    files = sorted(p.name for p in upload_dir.iterdir() if p.is_file())
    return {"documents": files}
