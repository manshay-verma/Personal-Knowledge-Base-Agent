from pathlib import Path

from app.ingestion.parsers import extract_pdf_text
from app.ingestion.chunker import chunk_text
from app.rag.embedder import Embedder


def test_embedder():
    pdf_path = Path("tests/sample.pdf")

    # Verify sample PDF exists
    assert pdf_path.exists(), f"Sample PDF not found: {pdf_path}"

    # Extract text
    text = extract_pdf_text(pdf_path)

    assert isinstance(text, str)
    assert len(text) > 0

    # Chunk text
    chunks = chunk_text(text)

    assert isinstance(chunks, list)
    assert len(chunks) > 0

    # Generate embeddings
    embedder = Embedder()
    embeddings = embedder.embed_documents(chunks)

    # Assertions
    assert isinstance(embeddings, list)
    assert len(embeddings) == len(chunks)

    # all-MiniLM-L6-v2 produces 384-dimensional vectors
    assert len(embeddings[0]) == 384

    # Optional output
    print(f"\nText length: {len(text)}")
    print(f"Chunks: {len(chunks)}")
    print(f"Embeddings: {len(embeddings)}")
    print(f"Embedding dimension: {len(embeddings[0])}")

    print("\nFirst chunk:")
    print(chunks[0][:200])

    print("\nFirst 10 embedding values:")
    print(embeddings[0][:10])