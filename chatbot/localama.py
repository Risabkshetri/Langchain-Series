from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Make sure LANGCHAIN_API_KEY exists before setting it
if os.getenv("LANGCHAIN_API_KEY"):
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
else:
    st.error("Please set your LANGCHAIN_API_KEY in the .env file")
    st.stop()

## Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please response to the user queries"),
    ("user", "Question:{question}")
])

## streamlit framework
st.title('Langchain Demo With LLAMA2 API')
input_text = st.text_input("Search the topic u want")

# ollama LLAma2 LLm
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    try:
        with st.spinner('Generating response...'):
            response = chain.invoke({"question": input_text})
            st.write(response)
    except Exception as e:
        st.error(f"Error: {str(e)}")