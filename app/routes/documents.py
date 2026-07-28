from pathlib import Path
import shutil

from fastapi import APIRouter, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.db.models import Document

from app.ingestion.parsers import extract_pdf_text
from app.ingestion.chunker import chunk_text

from app.rag.embedder import Embedder
from app.rag.vectorstore import VectorStore
from app.config import Settings

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
    )

UPLOAD_DIR = Path(Settings.upload_dir) 
UPLOAD_DIR.mkdir(parents=True, exist_ok = True)

@router.post("/upload")
async def upload_document(file:UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    file_path = UPLOAD_DIR/file.filename

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        text = extract_pdf_text(file_path)

        chunks = chunk_text(text)

        if not chunks:
            raise HTTPException(
                status_code= 400,
                detail="No chunks generated."
            )

        embedder = Embedder()
        embedding = embedder.embed_documents(chunks)

        metadata = [
            {
                "source" :file.filename,
                "chunk": i+1,
                "type":"document"
            }
            for i in range(len(chunks))
        ]

        vectorstore = VectorStore()
        vectorstore.add_documents(
            chunks=chunks,
            embedding=embedding,
            metadata=metadata,
        )

        db: Session = SessionLocal()
        try:
            document = Document(
                filename=file.filename,
                filepath = str(file_path)
            )
            db.add(document)
            db.commit()
            db.refresh(document)
        finally:
            db.close()

        return {
            "message":"Document upload successfully",
            "document_id":document.filename,
            "chunks":len(chunks),
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail = str(e),
        )