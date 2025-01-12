import requests
import streamlit as st

#openai client
def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke", json={"input": {"topic": input_text}})

    return response.json()['output']

# ollama client
def get_ollama_response(input_text):
    response=requests.post("http://localhost:8000/poem/invoke", json={"input": {"topic": input_text}})

    return response.json()['output']

st.title("Langchain API Client")
input_text1 = st.text_input("Enter a topic for essay")
input_text2 = st.text_input("Enter a topic for poem")

if input_text1:
    st.write(get_openai_response(input_text1))

if input_text2:
 st.write(get_ollama_response(input_text2))