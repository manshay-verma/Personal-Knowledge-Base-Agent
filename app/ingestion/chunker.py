from langchain.text_splitter import RecursiveCharacterTextSplitter

# 1 token = 4 char

TARGET_TOKEN = 400
CHUNK_SIZE = TARGET_TOKEN *400 # ~1600 CHAR
CHUNK_OVERLAP = 60*4           # ~240 char ~ 60 tokens

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = CHUNK_SIZE,
    chunk_overlap = CHUNK_OVERLAP,
    separators=[
        "\n\n",
        "\n",
        ".",
        " ",
        ""
    ]
)

def chunk_text(text:str)->list[str]:
    if not text or not text.strip():
        return []
    chunks = text_splitter.split_text(text)
    return [chunk.strip() for chunk in chunks if chunk.strip()]

 