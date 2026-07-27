from app.utils.citations import append_citations


def test_append_single_source_single_chunk():
    answer = "Python is dynamically typed."

    retrieved_chunks = [
        {
            "text": "Python is dynamically typed.",
            "metadata": {
                "source": "Python.pdf",
                "chunk": 1,
            },
        }
    ]

    result = append_citations(answer, retrieved_chunks)

    assert "Sources:" in result
    assert "Python.pdf (Chunk: 1)" in result


def test_append_single_source_multiple_chunks():
    answer = "Python supports OOP."

    retrieved_chunks = [
        {
            "text": "...",
            "metadata": {
                "source": "Python.pdf",
                "chunk": 1,
            },
        },
        {
            "text": "...",
            "metadata": {
                "source": "Python.pdf",
                "chunk": 2,
            },
        },
        {
            "text": "...",
            "metadata": {
                "source": "Python.pdf",
                "chunk": 3,
            },
        },
    ]

    result = append_citations(answer, retrieved_chunks)

    assert "Python.pdf (Chunks: 1, 2, 3)" in result


def test_append_multiple_sources():
    answer = "Answer"

    retrieved_chunks = [
        {
            "text": "...",
            "metadata": {
                "source": "Python.pdf",
                "chunk": 1,
            },
        },
        {
            "text": "...",
            "metadata": {
                "source": "ML.pdf",
                "chunk": 4,
            },
        },
    ]

    result = append_citations(answer, retrieved_chunks)

    assert "Python.pdf (Chunk: 1)" in result
    assert "ML.pdf (Chunk: 4)" in result


def test_append_empty_chunks():
    answer = "No documents found."

    result = append_citations(answer, [])

    assert result == answer


def test_append_missing_metadata():
    answer = "Answer"

    retrieved_chunks = [
        {
            "text": "...",
            "metadata": {},
        }
    ]

    result = append_citations(answer, retrieved_chunks)

    assert "Unknown" in result