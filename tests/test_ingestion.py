from app.ingestion.chunker import chunk_text
from app.ingestion.parsers import extract_text


def test_chunk_text_returns_chunks(tmp_path):
    file = tmp_path / "sample.md"
    file.write_text("hello world " * 20, encoding="utf-8")

    text = extract_text(file)
    chunks = chunk_text(text, chunk_size=10)

    assert text
    assert len(chunks) > 0
