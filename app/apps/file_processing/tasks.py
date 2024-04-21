```python
from celery import shared_task
from PyPDF2 import PdfFileReader
from pdfminer.high_level import extract_text
import os

@shared_task
def process_pdf(file_path):
    try:
        # Validate if it's a PDF
        with open(file_path, 'rb') as file:
            reader = PdfFileReader(file)
            if not reader.isEncrypted:
                info = reader.getDocumentInfo()
                if info.title is None and info.author is None:
                    raise ValueError("The file is not a valid PDF.")
        
        # Extract text from PDF
        text = extract_text(file_path)
        
        # Preprocess text
        text = preprocess_text(text)
        
        return text
    except Exception as e:
        # Log the error
        print(f"Error processing file {file_path}: {str(e)}")
        return None

def preprocess_text(text):
    # Remove unnecessary characters or formatting
    # This is a placeholder function, actual implementation will depend on the specific requirements
    return text.strip()
```