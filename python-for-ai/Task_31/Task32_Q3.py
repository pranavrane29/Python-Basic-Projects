from langchain_community.document_loaders import (PyPDFLoader,WebBaseLoader)


pdf_loader = PyPDFLoader("data/sample.pdf")

pdf_documents = pdf_loader.load()

wikipedia_url = (
    "https://en.wikipedia.org/wiki/"
    "Artificial_intelligence"
)

web_loader = WebBaseLoader(
    wikipedia_url
)

web_documents = web_loader.load()


print("=" * 50)
print("PDF DOCUMENT")
print("=" * 50)

print(
    "Number of PDF pages/documents loaded:",
    len(pdf_documents)
)


print("\n" + "=" * 50)
print("WIKIPEDIA DOCUMENT")
print("=" * 50)

print(
    "Number of web documents loaded:",
    len(web_documents)
)