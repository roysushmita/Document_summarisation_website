# Text Summarization App

## Overview
This text summarization website employs the powerful BART model(Bart large CNN), enabling users to succinctly summarize text, documents, or articles with ease. The platform offers a user-friendly interface where individuals can either input text directly or upload PDF files. Users have the flexibility to customize parameters such as minimum and maximum length to tailor the summary according to their preferences. The website harnesses the capabilities of the BART model to generate concise and coherent summaries...

Moreover, a notable feature of this text summarization website is its language versatility. It has the capability to summarize content from any language and translate it into another language seamlessly. This multilingual functionality enhances its utility for a diverse user base, allowing individuals to receive summaries in their preferred languages. The interactive nature of the platform makes it accessible and efficient for users seeking high-quality summaries in a language of their choice.

## Project Structure
- `Main.py`: The main Streamlit app script.
- `functions.py`: Module containing functions for PDF to text conversion and translation.

## Prerequisites
- Python 3.1
- Required Python packages: `streamlit`, `requests`, `googletrans==4.0.0-rc1`, `PyPDF2`
- API (You can access the API by making your own API key from HuggingFace website)
  
## Setup
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run
Run the following command in your terminal:
```bash
streamlit run Main.py 
```


 ## Additional Configurations 
 You can customize the background color and add graphics by modifying the Streamlit app script (Main.py).
  Place your images in the images/ directory.


## How to use
Open the app in your web browser.
Choose the input type: "Text" or "PDF".
Enter the text or upload a PDF file accordingly.
Set the summarization parameters using sliders.
Enter the target language code if translation is needed.
Click the "Generate Summary" button to get the summarized text.
API Key
To use the Hugging Face API, you need to obtain an API key. Set the API key in the headers dictionary in app.py.

## Acknowledgments 
This project uses the Hugging Face API for text summarization.
License
This project is licensed under the MIT License.

