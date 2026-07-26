from __future__ import annotations

from pathlib import Path
import pdfplumber


def extract_pdf_text(pdf_path:str|Path) -> str:
    pdf_path = Path(pdf_path)
    if not pdf_path:
        raise FileNotFoundError(f"File not Found:{pdf_path}")
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                pages.append(text.strip())

    extracted_text = "\n\n".join(pages).strip()

    if not extracted_text:
        raise ValueError("No text could be extract from the pdf")
    
    return extracted_text