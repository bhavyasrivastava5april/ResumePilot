from PyPDF2 import PdfReader

def extract_resume_text(filepath):
    reader = PdfReader(filepath)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text

    return resume_text