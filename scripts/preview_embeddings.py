from math import sqrt
from app.rag.embeddings import get_embedding_model


def cosine_similarity(
        first_vector:list[float],
        second_vector:list[float],
) -> float:
    '''Calculate how similar two embedding vectors are'''

    dot_product = sum(
        first * second
        for first, second in zip(first_vector, second_vector)
    )

    first_length = sqrt(sum(value ** 2 for value in first_vector))
    second_length = sqrt(sum(value ** 2 for value in second_vector))

    return dot_product / (first_length * second_length)

def main() -> None:
    embedding_model = get_embedding_model()

    query = "A PCB has an open circuit caused by a broken copper trace."

    related_text = (
        "A broken copper trace creates an open circuit and requires "
        "continuity testing."
    )

    less_related_text = (
        "The cafeteria menu includes pasta and salad."
    )

    query_vector = embedding_model.embed_query(query)

    document_vectors = embedding_model.embed_documents(
        [related_text, less_related_text]
    )

    related_score = cosine_similarity(
        query_vector,
        document_vectors[0],
    )

    less_related_score = cosine_similarity(
        query_vector,
        document_vectors[1],
    )

    print(f"Embedding dimensions: {len(query_vector)}")
    print(f"Related text similarity: {related_score:.3f}")
    print(f"Less-related text similarity: {less_related_score:.3f}")


if __name__ == "__main__":
    main()
