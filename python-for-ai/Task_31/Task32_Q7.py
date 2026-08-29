from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vector_store = Chroma(
    persist_directory="chroma-db",
    embedding_function=embeddings
)


retriever = vector_store.as_retriever(
    search_type="mmr"
)

question = input(
    "Ask a question about the document: "
)

retrieved_documents = retriever.invoke(
    question
)
print("\n" + "=" * 60)
print("RETRIEVED DOCUMENTS")
print("=" * 60)

print(
    "Number of documents retrieved:",
    len(retrieved_documents)
)


for i, document in enumerate(
    retrieved_documents,
    start=1
):

    print(f"\n--- Document {i} ---")
    print(document.page_content)