"""
File reading utilities for different document formats.
"""
import pdfplumber
from docx import Document


def read_txt(file) -> str:
    """Read and decode a plain text file."""
    return file.read().decode("utf-8")


def read_pdf(file) -> str:
    """Extract text from all pages of a PDF file."""
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


def read_docx(file) -> str:
    """Extract text from a DOCX file."""
    doc = Document(file)
    return " ".join(p.text for p in doc.paragraphs)


def read_uploaded_file(uploaded_file) -> str:
    """
    Read content from an uploaded file based on its MIME type.
    
    Args:
        uploaded_file: Streamlit uploaded file object
        
    Returns:
        Extracted text content from the file
    """
    if uploaded_file is None:
        return ""
    
    if uploaded_file.type == "text/plain":
        return read_txt(uploaded_file)
    elif uploaded_file.type == "application/pdf":
        return read_pdf(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return read_docx(uploaded_file)
    
    return ""
