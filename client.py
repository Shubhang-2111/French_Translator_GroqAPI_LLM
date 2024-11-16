import requests
import streamlit as st

def get_respone(input_text):
    json_body = {
  "input": {
    "language": "French",
    "text": input_text
  },
  "config": {},
  "kwargs": {}
}
    response = requests.post('http://localhost:8000/chain/invoke',json=json_body)

    return response.json().get("output","Not output found :(")

st.title("ENGLISH TO FRENCH CONVERTER uisng LLM ")

input_text=st.text_input("Enter the text you want to convert to french")

if input_text:
    st.write(get_respone(input_text))
