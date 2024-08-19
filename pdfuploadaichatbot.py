# -*- coding: utf-8 -*-
"""pdfuploadaichatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hPKfc7pJiMmmIaxyN30dDSlh62aNJKii
"""

from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

inputs = tokenizer("Hello, how are you?", return_tensors="pt")
outputs = model.generate(inputs.input_ids, max_length=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

!pip install transformers

from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load tokenizer and model - public access
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Example input text
input_text = "Once upon a time in a land far, far away"

# Tokenize and generate text
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(inputs.input_ids, max_length=100)

# Decode and print the generated text
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)

!pip install transformers PyPDF2

!pip install PyPDF2

from google.colab import files
from PyPDF2 import PdfReader

# Step to upload PDF
uploaded = files.upload()

# Function to read the PDF
def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

# Extract the text from the uploaded PDF
pdf_text = read_pdf(list(uploaded.keys())[0])
print(pdf_text)  # Optional: to see the extracted text

!pip install PyMuPDF transformers

from google.colab import files
import fitz  # PyMuPDF
from transformers import pipeline

# Upload the PDF file
uploaded = files.upload()
pdf_path = list(uploaded.keys())[0]
print("Uploaded file path:", pdf_path)

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Load a pre-trained question-answering model and tokenizer
qa_pipeline = pipeline('question-answering')

# Define a question
question = "What is the main topic of the PDF?"

# Get the answer
answer = qa_pipeline(question=question, context=pdf_text)
print("Answer:", answer['answer'])

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("question-answering", model="distilbert/distilbert-base-cased-distilled-squad")

# Load model directly
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-cased-distilled-squad")
model = AutoModelForQuestionAnswering.from_pretrained("distilbert/distilbert-base-cased-distilled-squad")

# Install required libraries
!pip install PyMuPDF transformers

from google.colab import files

# Upload the PDF file
uploaded = files.upload()

# Retrieve the file path
pdf_path = list(uploaded.keys())[0]
print("Uploaded file path:", pdf_path)

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Interactive question-answering loop
print("You can now ask questions about the PDF content. Type 'exit' to end.")
while True:
    # Get user input
    question = input("Ask a question: ")

    # Exit the loop if user types 'exit'
    if question.lower() == 'exit':
        print("Exiting the interactive session.")
        break

    # Get the answer
    answer = qa_pipeline(question=question, context=pdf_text)

    # Print the answer
    print("Answer:", answer['answer'])