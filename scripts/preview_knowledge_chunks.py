from app.rag.document_loader import load_knowledge_documents, split_knowledge_documents

def main() -> None:
    documents = load_knowledge_documents()
    chunks = split_knowledge_documents(documents)

    print(f'Loaded documents : {len(documents)}')
    print(f'Created chunks : {len(chunks)}')

    if not chunks:
        return

    first_chunk = chunks[0]

    print("\n--- First chunk metadata ---")
    print(first_chunk.metadata)

    print("\n--- First chunk content ---")
    print(first_chunk.page_content)
    

if __name__ == '__main__':
    main()