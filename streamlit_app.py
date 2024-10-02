
import streamlit as st
from PyPDF2 import PdfReader  # Library for PDF processing

st.title("Chatbot AI for Resume Evaluation")

# File uploader for resume
uploaded_file = st.file_uploader("Upload your resume (PDF format)", type='pdf')

if uploaded_file is not None:
    # Process the uploaded PDF and get recommendations
    reader = PdfReader(uploaded_file)
    text = ""
    
    # Extract text from each page of the PDF
    for page in reader.pages:
        text += page.extract_text()
    
    # Display the extracted text (for now)
    st.subheader("Extracted Text:")
    st.write(text)
