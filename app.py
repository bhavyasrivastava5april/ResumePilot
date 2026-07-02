from PyPDF2 import PdfReader
from flask import Flask, render_template, request
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        file = request.files['resume']
        job_description = request.form['job_description']

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        reader = PdfReader(filepath)

        resume_text = ""

        for page in reader.pages:
            text = page.extract_text()
            if text:
                resume_text += text

        # Convert both to lowercase
        resume_text = resume_text.lower()
        job_description = job_description.lower()

        # Split into words
        resume_words = set(resume_text.split())
        job_words = set(job_description.split())

        # Find matching words
        matched_words = resume_words.intersection(job_words)

        # Calculate score
        if len(job_words) != 0:
            score = round((len(matched_words) / len(job_words)) * 100, 2)
        else:
            score = 0

        return render_template(
            "result.html",
            score=score,
            matched=sorted(matched_words)
        )

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
