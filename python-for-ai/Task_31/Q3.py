from dotenv import load_dotenv

from langchain_huggingface import (
    HuggingFaceEndpoint,
    HuggingFacePipeline,
    ChatHuggingFace
)

from langchain_core.messages import HumanMessage


load_dotenv()

api_llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation",
    provider="auto",
    max_new_tokens=500
)

api_chat_model = ChatHuggingFace(
    llm=api_llm
)


local_llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 500
    }
)

local_chat_model = ChatHuggingFace(
    llm=local_llm
)


question = "What is the difference between AI and Machine Learning?"

message = HumanMessage(
    content=question
)


api_response = api_chat_model.invoke(
    [message]
)


local_response = local_chat_model.invoke(
    [message]
)

print("\n" + "=" * 60)
print("API MODEL RESPONSE")
print("=" * 60)

print(api_response.content)


print("\n" + "=" * 60)
print("LOCAL MODEL RESPONSE")
print("=" * 60)

print(local_response.content)

print("\n" + "=" * 60)
print("OBSERVATION")
print("=" * 60)

print("""
The API model, DeepSeek-R1, generally produces a more
detailed and higher-quality response because it is a much
larger and more capable model. However, it depends on an
internet connection and API access.

The local TinyLlama model runs directly on the computer and
does not require an API request after the model is downloaded.
It may provide responses faster or slower depending on the
computer hardware, but its response quality is generally more
limited compared to DeepSeek-R1.
""")