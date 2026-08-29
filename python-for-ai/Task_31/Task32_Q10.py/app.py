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

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a helpful college information assistant.

Answer the user's question using ONLY the
provided knowledge base context.

Do not use outside knowledge.

If the answer cannot be found in the
provided context, respond exactly:

"I could not find the answer."

Keep your answer clear and concise.
"""
        ),
        (
            "human",
            """
Knowledge Base Context:
{context}

User Question:
{question}
"""
        )
    ]
)


def answer_question(question):

    # Retrieve relevant documents
    retrieved_documents = retriever.invoke(
        question
    )

    # Combine retrieved chunks
    context = "\n\n".join(
        document.page_content
        for document in retrieved_documents
    )

    # Format the RAG prompt
    formatted_prompt = prompt.invoke(
        {
            "context": context,
            "question": question
        }
    )

    # Generate answer
    response = model.invoke(
        formatted_prompt
    )

    return response.content


print("=" * 60)
print("COLLEGE RULES RAG CHATBOT")
print("=" * 60)

print(
    "Ask questions about the college rules."
)

print(
    "Type 'exit' to close the chatbot."
)


while True:

    question = input(
        "\nYou: "
    )


    # Exit chatbot
    if question.lower().strip() == "exit":

        print(
            "\nBot: Goodbye!"
        )

        break

    if not question.strip():

        print(
            "Bot: Please enter a question."
        )

        continue


    try:

        answer = answer_question(
            question
        )

        print(
            "\nBot:",
            answer
        )


    except Exception as error:

        print(
            "\nError:",
            error
        )