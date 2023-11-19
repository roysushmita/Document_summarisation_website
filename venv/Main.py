#importing necessary libraries

import streamlit as st
import requests
from googletrans import Translator
import io
import os
import PyPDF2
from functions import convert_pdf_to_txt,translate_to_english,translate_summarised_text


#fetching the BART LARGE LANGUAGE MODEL using API
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}

st.title("Text Summarization")


option = st.radio("Choose Input Type:", ("Text", "PDF"))

if option == "Text":
    data = st.text_area("Enter Text:", "Enter your text here")
elif option == "PDF":
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_file is not None:
        file_contents = uploaded_file.read()
        data = convert_pdf_to_txt(file_contents)





min_length = st.slider("Minimum Length:", min_value=1, max_value=500, value=50)
max_length = st.slider("Maximum Length:", min_value=1, max_value=500, value=150)

target_language1 = st.text_input("Enter the target language code (e.g., hindi, Telugu , Tamil ):", 'English').lower()


 


# Function to make API request
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


if st.button("Generate Summary"):
    # Translate the input text to the specified target language
    translated_text = translate_to_english(data,is_text_area=(option == "Text"))

    # Make API request
    summ_text = query({"inputs": translated_text, "parameters": {"min_length": min_length, "max_length": max_length}})
    
    if summ_text and isinstance(summ_text, list):
        # Extract the summary text from the dictionary in the list
        summary_text = summ_text[0]['summary_text']

    output = translate_summarised_text(summary_text, target_language=target_language1)
    

    st.subheader("Summary:")
    st.write(output)
