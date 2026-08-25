from langchain_huggingface import (
    HuggingFacePipeline,
    ChatHuggingFace
)

from langchain_core.messages import HumanMessage

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 1000
    }
)

chat_model = ChatHuggingFace(
    llm=llm
)

response = chat_model.invoke(
    [
        HumanMessage(
            content="Introduce Yourself in 100 words"
        )
    ]
)

print(response.content)