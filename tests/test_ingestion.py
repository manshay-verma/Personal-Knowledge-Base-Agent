
from pathlib import Path
from app.ingestion.parsers import extract_pdf_text


def test_pdf_parser():
    pdf_file = Path("tests/sample.pdf")

    text = extract_pdf_text(pdf_file)

    assert isinstance(text, str)
    assert len(text) > 0

    print("\nExtracted Text:\n")
    print(text[:500])


from app.ingestion.parsers import extract_pdf_text
from app.ingestion.chunker import chunk_text
from app.rag.embedder import Embedder
from app.rag.vectorstore import VectorStore


def test_vectorstore():

    # Parse PDF
    text = extract_pdf_text("tests/sample.pdf")

    # Chunk
    chunks = chunk_text(text)

    # Embeddings
    embedder = Embedder()
    embeddings = embedder.embed_documents(chunks)

    # Vector DB
    db = VectorStore()

    db.reset()

    db.add_documents(
        chunks,
        embeddings,
        metadata=[
            {
                "source": "sample.pdf",
                "chunk": i,
            }
            for i in range(len(chunks))
        ],
    )

    assert db.count() == len(chunks)

    query = "What is Retrieval Augmented Generation?"

    query_embedding = embedder.embed_query(query)

    results = db.similarity_search(query_embedding)

    assert len(results["documents"][0]) > 0

    print("\nTop Result:\n")
    print(results["documents"][0][0])

from app.ingestion.parsers import extract_pdf_text
from app.ingestion.chunker import chunk_text
from app.rag.embedder import Embedder
from app.rag.vectorstore import VectorStore
from app.rag.retriever import Retriever


def test_retriever():

    # Parse PDF
    text = extract_pdf_text("tests/sample.pdf")

    # Chunk
    chunks = chunk_text(text)

    # Embeddings
    embedder = Embedder()
    embeddings = embedder.embed_documents(chunks)

    # Store in Chroma
    db = VectorStore()
    db.reset()

    db.add_documents(
        chunks,
        embeddings,
        metadata=[
            {
                "source": "sample.pdf",
                "chunk": i,
            }
            for i in range(len(chunks))
        ],
    )

    # Retrieve
    retriever = Retriever(
        embedder=embedder,
        vectorstore=db,
    )

    results = retriever.retrieve(
        "What is Retrieval Augmented Generation?",
        k=5,
    )

    assert len(results) > 0

    print("\nRetrieved Chunks\n")

    for i, result in enumerate(results, start=1):
        print("=" * 60)
        print(f"Rank {i}")
        print(f"Distance : {result['distance']:.4f}")
        print(f"Metadata : {result['metadata']}")
        print()
        print(result["text"][:300])
        print()
