from app.rag.vectorstore import VectorStore


def test_vectorstore_initializes(tmp_path):
    store = VectorStore(persist_dir=str(tmp_path))
    assert store.collection is not None
