import streamlit as st
from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

## load the GROQ And OpenAI API KEY 
groq_api_key=os.getenv('GROQ_API_KEY')
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

llm=ChatGroq(groq_api_key=groq_api_key,model_name="Llama3-8b-8192",temperature=1)




if selected=="Simple Chat-Bot":
    st.header('Simple :blue[_Chat-Bot_] :sunglasses:',divider='rainbow')
    def generate_result():
        prompt=st.chat_input("Type something here")
        
        if prompt:
            response=llm.invoke(prompt)
            st.markdown(response.content)

    if __name__ == "__main__":
        generate_result()