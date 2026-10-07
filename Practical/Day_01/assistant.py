from openai import OpenAI
#from google import genai
from dotenv import load_dotenv
import os

# Load configuartion from the .env file
load_dotenv()

# Create a client  that communicates with Ollama
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

#Send question to the AI Model
print("=" * 40)
print("Welcome to the AI Chatbot")
print("=" * 40)

while True:
    question = input("What can I do for you today? : ").strip()

    if question.lower() == "quit":
        print("Thank you for using the AI Chatbot. Goodbye!")
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
               "role": "system",
               "content": "Answer briefly. Do not add extra context, explanations, examples, or follow-up questions."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    print(response.choices[0].message.content)