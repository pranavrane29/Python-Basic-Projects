import os

from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise ValueError(
        "GROQ_API_KEY is not set. "
        "Please add it to the .env file."
    )

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


model = init_chat_model(
    model="openai/gpt-oss-20b",
    model_provider="groq"
)

prompt = ChatPromptTemplate.from_template(
    """
You are a helpful AI assistant.

Answer the question using ONLY the provided context.

If the answer is not found in the context,
say exactly:

"I could not find the answer."

Context:
{context}

Question:
{question}

Answer:
"""
)

def answer_question(question):

    retrieved_documents = retriever.invoke(
        question
    )

    context = "\n\n".join(
        document.page_content
        for document in retrieved_documents
    )

    formatted_prompt = prompt.invoke(
        {
            "context": context,
            "question": question
        }
    )

    response = model.invoke(
        formatted_prompt
    )

    return response.content


print("=" * 60)
print("COMPLETE RAG APPLICATION")
print("=" * 60)

print("Type 'exit' to stop.")


while True:

    question = input(
        "\nAsk a question: "
    )

    if question.lower() == "exit":
        print("Goodbye!")
        break

    if not question.strip():
        print("Please enter a question.")
        continue

    try:

        answer = answer_question(
            question
        )

        print("\nFinal Answer:")
        print(answer)

    except Exception as error:

        print(
            "\nError:",
            error
        )