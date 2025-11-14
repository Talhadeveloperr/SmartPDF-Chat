from PyPDF2 import PdfReader

def load_pdf_text(pdf_file):
    """Extracts text from each page of an uploaded PDF file."""
    pdf = PdfReader(pdf_file)
    texts = [page.extract_text() for page in pdf.pages if page.extract_text()]
    return texts
