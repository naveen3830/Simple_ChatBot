import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()

headers={
    "authorization":st.secrets["groq_api_key"],
    "content-type":"application/json"
}

# Load the GROQ and Google API keys
groq_api_key = os.getenv('GROQ_API_KEY')
# os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Initialize the language model
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192", temperature=1)

# Set the header of the Streamlit app
st.header('Simple :blue[_Chat-Bot_] :sunglasses:', divider='rainbow')

def generate_result():
    prompt = st.chat_input("Type something here")
    
    if prompt:
        response = llm.invoke(prompt)
        st.markdown(response.content)
        
        
        # num_lines = generated_text.count('\n') + 1
        # st.text_area("Generated Response", generated_text, height=num_lines * 20)

if __name__ == "__main__":
    generate_result()
