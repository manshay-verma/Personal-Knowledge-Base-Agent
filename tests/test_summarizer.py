from app.memory.summarizer import ConversationSummarizer


def test_summarizer():

    conversation = """
User:
I am learning Python.

Assistant:
Great!

User:
I also want to learn FastAPI.
"""

    summarizer = ConversationSummarizer()

    summary = summarizer.summarize(conversation)

    assert isinstance(summary, str)
    assert len(summary) > 20

    print(summary)