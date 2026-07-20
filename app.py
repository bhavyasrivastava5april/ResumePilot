from flask import send_file
from utils.pdf_generator import generate_pdf
from utils.suggestions import generate_recommendation
from flask import Flask, render_template, request
import os

from utils.extractor import extract_resume_text
from utils.analyzer import calculate_ats_score
from utils.section_checker import check_resume_sections

app = Flask(__name__)
latest_report = {}

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
        found_sections, missing_sections = check_resume_sections(resume_text)

        # Calculate ATS score
        score, matched_skills, missing_skills = calculate_ats_score(
            resume_text,
            job_description
        )

        # Generate suggestions
        recommendation= generate_recommendation(
            score,
            missing_skills,
            missing_sections
        )
        latest_report["score"] = score
        latest_report["matched_skills"] = matched_skills
        latest_report["missing_skills"] = missing_skills
        latest_report["recommendation"] = recommendation
        latest_report["found_sections"] = found_sections
        latest_report["missing_sections"] = missing_sections

        return render_template(
            "result.html",
            score=score,
            matched_skills=matched_skills,
            missing_skills=missing_skills,
            found_sections=found_sections,
            missing_sections=missing_sections,
            recommendation=recommendation
        )

    return render_template("index.html")


@app.route("/download-report")
def download_report():

    pdf = generate_pdf(
        latest_report["score"],
        latest_report["matched_skills"],
        latest_report["missing_skills"],
        latest_report["recommendation"],
        latest_report["found_sections"],
        latest_report["missing_sections"],
    )

    return send_file(
        pdf,
        download_name="ResumePilot_Report.pdf",
        as_attachment=True,
        mimetype="application/pdf",
    )


if __name__ == '__main__':
    app.run(debug=True)
    