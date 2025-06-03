import pytesseract
from pdf2image import convert_from_bytes
import re

def extract_text_from_pdf(pdf_bytes):
    images = convert_from_bytes(pdf_bytes, dpi=300)
    text = ""
    for img in images:
        raw = pytesseract.image_to_string(img, lang='por')
        text += raw + "\n"
    return clean_text(text)

def clean_text(text):
    text = text.replace('-\n', '')
    text = re.sub(r'[ \t]+\n', '\n', text)
    text = re.sub(r'\n{2,}', '\n\n', text)
    return text.strip()