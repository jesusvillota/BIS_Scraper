from __future__ import annotations
import os
import PyPDF2
from typing import Union, List


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        Extracted text from the PDF
        
    Raises:
        Exception: If the PDF file cannot be processed
    """
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
    return text


def process_pdfs(pdf_dir: str, text_dir: str, specific_files: Union[List[str], None] = None) -> None:
    """Process PDF files in a directory and extract text.
    
    Args:
        pdf_dir: Directory containing PDF files
        text_dir: Directory to save extracted text files
        specific_files: Optional list of specific PDF files to process
    """
    # Create text directory if it doesn't exist
    os.makedirs(text_dir, exist_ok=True)
    
    # Get the list of PDF files to process
    if specific_files:
        pdf_files = [f for f in specific_files if f.lower().endswith('.pdf')]
    else:
        pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_file)
        print(f"\n👁️‍🗨️ Extracting: {pdf_path}")
        try:
            text = extract_text_from_pdf(pdf_path)
            
            # Save extracted text to file
            txt_filename = os.path.splitext(pdf_file)[0] + ".txt"
            txt_path = os.path.join(text_dir, txt_filename)
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"📩 Saved text to {txt_path}")
        except Exception as e:
            print(f"❌ Error processing {pdf_path}: {e}")
