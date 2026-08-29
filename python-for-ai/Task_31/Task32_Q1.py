import os

from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise ValueError(
        "GROQ_API_KEY is not set. "
        "Please add it to the .env file."
    )


model = init_chat_model(
    model="openai/gpt-oss-20b",
    model_provider="groq"
)


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI assistant."
        ),
        (
            "human",
            "{user_input}"
        )
    ]
)

print("=" * 50)
print("BASIC LLM CHAT APPLICATION")
print("=" * 50)
print("Type 'exit' to quit.")


while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("AI: Goodbye!")
        break

    if not user_input.strip():
        print("AI: Please enter a message.")
        continue

    try:
        formatted_prompt = prompt.invoke(
            {
                "user_input": user_input
            }
        )

        response = model.invoke(formatted_prompt)
        
        print("\nAI:", response.content)
    except Exception as error:
        print("\nError while generating response:",error)