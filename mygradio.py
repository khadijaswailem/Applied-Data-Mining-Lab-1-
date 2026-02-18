import os #to access environment variables (like API key)
from dotenv import load_dotenv #allows to load variables from a .env file into environment
from groq import Groq #sends requests to Groq’s LLM API
import gradio as gr

# Load API key from .env
load_dotenv() #reads the .env
client = Groq(api_key=os.getenv("GROQ_API_KEY")) #Creates a Groq client object using that API key ,
#Now client can send requests to Groq

# Chat function
def chat_with_groq(message, history): #takes user message and conversation history as input
    if history is None: #if theres no history, initialize it as an empty list
        history = []

    history.append({"role": "user", "content": message})# Add user message to history with role "user"

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=history #so that model can generate a response based on the entire conversation history
    )

    reply = response.choices[0].message.content #Extract the generated reply from the API response
    history.append({"role": "assistant", "content": reply}) #Adds the assistant's reply to history

    return history, "" #updated chat history and empty string to clear the input box

# Custom pink button styling
pink_css = """
#submit-btn {
    background-color: #ff69b4 !important;
    color: white !important;
    border: none !important;
}
#submit-btn:hover {
    background-color: #ff1493 !important;
}
"""

# Gradio UI
with gr.Blocks(css=pink_css) as demo:
    gr.Markdown("# Ask Dija ")

    chatbot = gr.Chatbot()
    state = gr.State([])

    with gr.Row():
        msg = gr.Textbox(
            placeholder="Type your message here...",
            show_label=False,
            submit_btn=True  # disables enter-to-submit
        )
        submit_btn = gr.Button("Submit", elem_id="submit-btn")

    # Connect button click to chat function
    submit_btn.click(chat_with_groq, [msg, state], [chatbot, msg])

demo.launch()
