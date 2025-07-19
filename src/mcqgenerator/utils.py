import os
import json
import traceback
from PyPDF2 import PdfReader
from PyPDF2 import PdfReader

def read_file(uploaded_file):
    if uploaded_file.name.endswith('.pdf'):
        try:
            reader = PdfReader(uploaded_file)
            text = ''
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            return text
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return None
    elif uploaded_file.name.endswith('.txt'):
        try:
            return uploaded_file.read().decode('utf-8')
        except Exception as e:
            print(f"Error reading TXT: {e}")
            return None
    else:
        print("Unsupported file type.")
        return None


