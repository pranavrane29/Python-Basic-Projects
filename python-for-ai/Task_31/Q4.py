from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate


load_dotenv()


model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a very polite and helpful AI assistant."
        ),
        (
            "human",
            "{user_input}"
        )
    ]
)

user_input = input(
    "Enter your question: "
)

formatted_prompt = prompt.invoke(
    {
        "user_input": user_input
    }
)

response = model.invoke(
    formatted_prompt
)

print("\nAI Response:")
print(response.content)