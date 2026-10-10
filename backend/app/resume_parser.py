from pypdf import PdfReader
from io import BytesIO


def extract_text_from_pdf(file_content: bytes) -> str:
    """
    Extract text from a PDF resume.
    """

    if not file_content:
        raise ValueError("The uploaded PDF file is empty.")

    pdf_file = BytesIO(file_content)

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text.strip()