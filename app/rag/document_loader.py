from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
KNOWLEDGE_DIRECTORY = PROJECT_ROOT / 'data' / 'knowledge'

CHUNK_SIZE = 700
CHUNK_OVERLAP = 100

def load_knowledge_documents() -> list[Document]:
    '''Read all Markdown knowledge files as LangChain documents'''

    documents = []

    for file_path in KNOWLEDGE_DIRECTORY.rglob('*.md'):
        content = file_path.read_text(encoding='utf-8')

        document = Document(
            page_content = content,
            metadata={
                'source' : str(file_path.relative_to(PROJECT_ROOT)),
                'filename' : file_path.name
            },
        )

        documents.append(document)

    return documents

def split_knowledge_documents(documents : list[Document]) -> list[Document]:
    '''Split long knowledge documents into overlapping chunks'''

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    return text_splitter.split_documents(documents)
