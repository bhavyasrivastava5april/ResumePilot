from utils.skills import extract_skills


def calculate_ats_score(resume_text, job_description):

    # Extract skills from resume and job description
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    print("Resume Skills:", resume_skills)
    print("Job Skills:", job_skills)

    # Find common skills
    matched_skills = list(set(resume_skills) & set(job_skills))

    # Find missing skills
    missing_skills = list(set(job_skills) - set(resume_skills))

    # Calculate ATS Score
    if len(job_skills) > 0:
        score = round((len(matched_skills) / len(job_skills)) * 100, 2)
    else:
        score = 0

    return score, matched_skills, missing_skills