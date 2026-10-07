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

#Creating a list to store the conversation history (memory) between the user and the AI assistant. This allows the AI to maintain context across multiple interactions.
mem_messages = []

while True:
    question = input("What can I do for you today? : ").strip()
    # Store the user's question in the conversation history (memory) with the role "user". This allows the AI to understand the context of the conversation and provide more relevant responses.
    mem_messages.append({"role": "user", "content": question})  # Store user message in memory
    if question.lower() == "quit":
        print("Thank you for using the AI Chatbot. Goodbye!")
        break
    
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=mem_messages
    )
    print(response.choices[0].message.content)
    # Store the assistant's response in the conversation history (memory) with the role "assistant". This allows the AI to maintain context and provide more coherent responses in future interactions.
    mem_messages.append({"role": "assistant", "content": response.choices[0].message.content})  # Store assistant message in memory