from app.rag.rag_prompt import RAG_PROMPT_TEMPLATE

def build_rag_prompt(
        question:str,
        retrieved_chunks:list[dict],
)->str:
    context = "\n\n".join(
        chunk["text"]
        for chunk in retrieved_chunks
    )
    return RAG_PROMPT_TEMPLATE.format(
        context=context,
        question=question,
    )