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

response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {
            "role":"user",
            "content":"What is a Elephant"
        }
    ])

# Display the response  
print(response.choices[0].message.content) 