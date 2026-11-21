from dotenv import load_dotenv
import os
load_dotenv()


def main() -> None:
    print("Hello from langchain-course-learninng!")
    print(os.environ.get("OEPNAI_API_KEY"))

if __name__ == "__main__":
    main()