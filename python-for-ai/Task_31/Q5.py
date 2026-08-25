import os

from dotenv import load_dotenv

from langchain_huggingface import (
    HuggingFaceEndpoint,
    HuggingFacePipeline,
    ChatHuggingFace
)

from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


def create_api_model():

    api_token = os.getenv(
        "HUGGINGFACEHUB_API_TOKEN"
    )

    if not api_token:
        raise ValueError(
            "HUGGINGFACEHUB_API_TOKEN is missing. "
            "Please add it to the .env file."
        )

    llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-R1",
        task="text-generation",
        provider="auto",
        max_new_tokens=500
    )

    chat_model = ChatHuggingFace(
        llm=llm
    )

    return chat_model


def create_local_model():

    llm = HuggingFacePipeline.from_model_id(
        model_id=(
            "TinyLlama/"
            "TinyLlama-1.1B-Chat-v1.0"
        ),
        task="text-generation",
        pipeline_kwargs={
            "max_new_tokens": 500
        }
    )

    chat_model = ChatHuggingFace(
        llm=llm
    )

    return chat_model


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


def main():

    print("=" * 50)
    print("WELCOME TO DUAL MODE CHATBOT")
    print("=" * 50)

    print("\nChoose chatbot mode:")
    print("1. API Mode")
    print("2. Local Mode")

    choice = input(
        "\nEnter your choice (1 or 2): "
    )


    try:

        if choice == "1":

            print(
                "\nLoading API model..."
            )

            chat_model = create_api_model()

            print(
                "API Mode selected."
            )


        elif choice == "2":

            print(
                "\nLoading local model..."
            )

            chat_model = create_local_model()

            print(
                "Local Mode selected."
            )


        else:

            print(
                "\nInvalid choice."
            )

            return


    except Exception as error:

        print(
            "\nError loading model:"
        )

        print(error)

        return


    print(
        "\nType 'exit' to stop the chatbot."
    )


    while True:

        user_input = input(
            "\nYou: "
        )


        if user_input.lower() == "exit":

            print(
                "\nChatbot: Goodbye! Have a nice day."
            )

            break

        if not user_input.strip():

            print(
                "Chatbot: Please enter a message."
            )

            continue


        try:

            formatted_prompt = prompt.invoke(
                {
                    "user_input": user_input
                }
            )

            response = chat_model.invoke(
                formatted_prompt
            )


            print(
                "\nChatbot:"
            )

            print(
                response.content
            )

        except Exception as error:

            print(
                "\nError generating response:"
            )

            print(error)


if __name__ == "__main__":

    main()