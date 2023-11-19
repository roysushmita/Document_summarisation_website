import streamlit as st
import requests
from googletrans import Translator
import io
import os
import PyPDF2

#for converting pdf to text
def convert_pdf_to_txt(pdf_content):
    pdf_file = io.BytesIO(pdf_content)
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text



#Converting other languages into English
def translate_to_english(text, is_text_area=True):
    if is_text_area:
        translator = Translator()
        translation = translator.translate(text, dest='en')
        return translation.text
    else:
        return text
    
#translating summarised text to other language
def translate_summarised_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text