import os
from dotenv import load_dotenv
from groq import Groq

# Load .env
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("Welcome to your Groq chat! Type 'exit' to quit.")

while True:
    # Ask the user for input
    user_input = input("You: ")
    
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    # Send the message to Groq LLM
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": user_input}],
        model="llama-3.1-8b-instant"  # or your chosen supported model
    )

    # Print Groq’s reply
    print("Groq:", response.choices[0].message.content)
