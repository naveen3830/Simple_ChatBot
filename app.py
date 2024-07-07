import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set the header of the Streamlit app
st.header('Simple :blue[_Chat-Bot_] :sunglasses:', divider='rainbow')

# Create a text input for the API key
groq_api_key = st.text_input("Enter your Groq API key:", type="password")

# Initialize the language model if API key is provided
llm = None

def generate_result():
    global llm
    
    if not groq_api_key:
        st.warning("Please enter your Groq API key to use the chat-bot.")
        return

    if llm is None:
        try:
            llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192", temperature=1)
        except Exception as e:
            st.error(f"Error initializing the model: {str(e)}")
            return

    prompt = st.chat_input("Type something here")
    
    if prompt:
        try:
            response = llm.invoke(prompt)
            st.markdown(response.content)
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")

if __name__ == "__main__":
    generate_result()
