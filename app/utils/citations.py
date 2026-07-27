from collections import defaultdict

def append_citations(
        answer:str,
        retrieved_chunks: list[dict]
)->str:
    grouped_source = defaultdict(set)
    for chunk in retrieved_chunks:
        metadata = chunk.get("metadata",{})
        source = metadata.get("source","Unkown")
        chunk_id = metadata.get("chunk")

        if chunk_id is not None:
            grouped_source[source].add(chunk_id)
        else:
            grouped_source[source]

    if not grouped_source:
        return answer

    citation_lines = ["\n\nSource:"]
    for source, chunk_ids in grouped_source.items():
        chunk_ids= sorted(chunk_ids)

        if len(chunk_ids) == 1:
            citation_lines.append(
                f"-{source}(Chunk:{chunk_ids[0]})"
            )
        else:
            chunks = ",".join(map(str,chunk_ids))
            citation_lines.append(
                f"-{source}(Chunks:{chunks})"
            )
    return answer + "\n" + "\n".join(citation_lines)

