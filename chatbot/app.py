from langchain_openai import chatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import strOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANCHAIN_API_KEY"] = os.getenv("LANCHAIN_API_KEY")


## prompt template

prompt = ChatPromptTemplate.from_message[
    ("system", "You are a helpful assistant. Please response to the user qiueries."),
    ("user", "Question:{question}"),
]

## streamlit framework
st.title("chatbot")
input_text = st.text_input("Enter your question here")

## OpenAI chatbot
llm=chatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))
output_parser = strOutputParser()
chain=prompt | llm | output_parser

if(input_text):
    st.write(chain.invoke({"question":input_text}))