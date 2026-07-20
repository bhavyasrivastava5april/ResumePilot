def generate_recommendation(score, missing_skills, missing_sections):
    """
    Generate one personalized recommendation based on the resume analysis.
    """

    # Low ATS score
    if score < 60:
        return (
            "Your resume has a low match with this job description. Review the required "
            "skills and responsibilities, then update your resume by emphasizing relevant "
            "skills, projects, and experience. Use keywords from the job description "
            "naturally, but only if they genuinely reflect your qualifications."
        )

    # Missing important resume sections
    elif missing_sections:
        sections = ", ".join(missing_sections)

        return (
            f"Your resume is missing important section(s): {sections}. Adding these "
            "sections can improve ATS compatibility and help recruiters quickly "
            "understand your qualifications."
        )

    # Missing skills
    elif missing_skills:
        skills = ", ".join(missing_skills[:5])

        if len(missing_skills) > 5:
            skills += ", and more"

        return (
            f"The job description highlights skills such as {skills}. If you have "
            "experience with these technologies, include them in your Skills section "
            "and demonstrate them through relevant projects or work experience."
        )

    # Excellent resume
    else:
        return (
            "Your resume aligns well with the provided job description. Before applying, "
            "review it once to ensure your achievements are measurable, your experience "
            "is up to date, and your projects clearly demonstrate your technical skills."
        )