from app.rag.rag_prompt import RAG_PROMPT_TEMPLATE

MAX_CONTEXT_CHARS = 5000

def build_rag_prompt(
        question:str,
        retrieved_chunks:list[dict],
)->str:
    context = "\n\n".join(
        chunk["text"]
        for chunk in retrieved_chunks
    )

    if len(context) > MAX_CONTEXT_CHARS:
        context = context[:MAX_CONTEXT_CHARS]

    return RAG_PROMPT_TEMPLATE.format(
        context=context,
        question=question,
    )