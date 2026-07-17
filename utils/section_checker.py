SECTION_KEYWORDS = {
    "Contact Information": ["email", "phone", "linkedin"],
    "Education": ["education", "college", "university"],
    "Skills": ["skills", "technical skills"],
    "Projects": ["projects", "project"],
    "Experience": ["experience", "work experience", "internship"],
    "Certifications": ["certification", "certifications"],
}


def check_resume_sections(resume_text):
    text = resume_text.lower()

    found_sections = []
    missing_sections = []

    for section, keywords in SECTION_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            found_sections.append(section)
        else:
            missing_sections.append(section)

    return found_sections, missing_sections