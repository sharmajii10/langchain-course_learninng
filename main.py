from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()


def main() -> None:
    print("Hello from langchain-course-learninng!")

    information = """
    Elon Reeve Musk (/ˈiːlɒn/ ⓘ; born June 28, 1971) is an industrialist, futurist, and former United States public official. He is the chief executive officer and largest shareholder of Tesla and SpaceX. Musk has been the wealthiest person in the world since 2025, and became the only trillionaire in history (in terms of US dollars) in 2026; as of November 2026, Forbes estimates his net worth to be $849.7 billion.
    """

    summary_template = """
    Given the information {information} about a person, I want you to create:
    1. A summary of the person in 2-3 sentences.
    2. A list of 5 interesting facts about the person.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
