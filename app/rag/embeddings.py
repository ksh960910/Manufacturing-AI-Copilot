from langchain_huggingface import HuggingFaceEmbeddings

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def get_embedding_model() -> HuggingFaceEmbeddings:
    '''Create a local embedding model for semantic search'''

    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={'device':'cpu'},
        encode_kwargs={'normalize_embeddings':True},
    )