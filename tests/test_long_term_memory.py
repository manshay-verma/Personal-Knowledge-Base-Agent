from app.memory.long_term_memory import LongTermMemory

def test_store_memory():
    memory = LongTermMemory()
    summary = (
        "The user is learning Python and FastAPI"
    )
    memory.store_memory(
        summary,
        metadata={
            "type":"conversation",
        },
    )
    assert memory.vectorstore.count() > 0

def test_search_memory():
    memory = LongTermMemory()
    result = memory.search_memory(
        "Python"
    )
    assert isinstance(result, dict)

def test_retrieve_memory():

    memory = LongTermMemory()

    breakpoint()
    memory.store_memory(
        "The user is learning Python."
    )
    results = memory.retrieve_memories(
        "Python"
    )

    assert len(results["documents"]) > 0