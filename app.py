from flask import Flask, render_template, request
import os

from utils.extractor import extract_resume_text
from utils.analyzer import calculate_ats_score

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        file = request.files['resume']
        job_description = request.form['job_description']

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Extract text from the resume
        resume_text = extract_resume_text(filepath)

        # Calculate ATS score
        score, matched_skills, missing_skills = calculate_ats_score(
    resume_text,
    job_description
)
        

        return render_template(
    "result.html",
    score=score,
    matched_skills=matched_skills,
    missing_skills=missing_skills
)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
