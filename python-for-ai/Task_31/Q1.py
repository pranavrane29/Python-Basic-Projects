from dotenv import load_dotenv

from langchain_huggingface import (
    HuggingFaceEndpoint,
    ChatHuggingFace
)

from langchain_core.messages import HumanMessage

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation",
    provider="auto",
    max_new_tokens=1000
)

chat_model = ChatHuggingFace(llm=llm)

response = chat_model.invoke(
    [
        HumanMessage(
            content="Introduce yourself."
        )
    ]
)
print(response.content)