from app.llm.groq_client import GroqClient


def test_groq():

    client = GroqClient()

    response = client.generate(
        "Explain Retrieval Augmented Generation in one sentence."
    )

    assert isinstance(response, str)
    assert len(response) > 0

    print("\nGroq Response:\n")
    print(response)