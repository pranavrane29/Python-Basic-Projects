from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template(
    """
You are a helpful AI assistant.

Answer the question using ONLY the provided context.

If the answer is not found in the context, say:
"I could not find the answer."

Context:
{context}

Question:
{question}

Answer:
"""
)

context = """
NovaTech Solutions is a fictional technology company
founded in 2020.

The company specializes in artificial intelligence,
cloud computing, and software development.

NovaTech Solutions is headquartered in Pune, India.
"""

question = "What does NovaTech Solutions specialize in?"

formatted_prompt = prompt.invoke(
    {
        "context": context,
        "question": question
    }
)

print("Formatted RAG Prompt:")
print(formatted_prompt.to_messages())