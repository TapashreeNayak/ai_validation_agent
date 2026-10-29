
from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

BASE_DIR = Path(__file__).resolve().parent
KNOWLEDGE_DIR = BASE_DIR / "knowledge_base"
CHROMA_DIR = BASE_DIR / "chroma_db"

# Load the instruction documents.
loader = DirectoryLoader(
    str(KNOWLEDGE_DIR),
    glob="*.md",
    show_progress=True,
)

documents = loader.load()

# Mark these as demonstration documents.
# Replace this with metadata from an authorized document
# registry when using real approved policies.
for document in documents:
    document.metadata["approval_status"] = "DEMO_APPROVED"

# Split documents into smaller searchable chunks.
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=120,
)

chunks = splitter.split_documents(documents)

# Generate embeddings locally.
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Persist vectors to disk.
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="frc_approved_instructions",
    persist_directory=str(CHROMA_DIR),
)

print(f"Loaded {len(documents)} documents.")
print(f"Created {len(chunks)} searchable chunks.")
print(f"ChromaDB location: {CHROMA_DIR}")


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    collection_name="frc_approved_instructions",
    persist_directory=str(CHROMA_DIR),
    embedding_function=embeddings,
)


def retrieve_frc_evidence(finding: dict, k: int = 3) -> list[dict]:
    """Retrieve relevant demonstration-approved instructions."""

    query = (
        f"Rule ID: {finding.get('Rule_ID', '')}\n"
        f"Error code: {finding.get('Error_Code', '')}\n"
        f"Validation message: {finding.get('Message', '')}"
    )

    docs = vectorstore.similarity_search(
        query,
        k=k,
        filter={"approval_status": "DEMO_APPROVED"},
    )

    return [
        {
            "source": Path(doc.metadata.get("source", "unknown")).name,
            "evidence": doc.page_content,
        }
        for doc in docs
    ]

