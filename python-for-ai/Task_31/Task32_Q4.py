from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader(
    "data/company_info.txt"
)

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(
    documents
)

print(
    "Total number of chunks created:",
    len(chunks)
)


print("\n" + "=" * 60)
print("FIRST FEW CHUNKS")
print("=" * 60)


for i, chunk in enumerate(
    chunks[:3],
    start=1
):

    print(f"\n--- Chunk {i} ---")
    print(chunk.page_content)