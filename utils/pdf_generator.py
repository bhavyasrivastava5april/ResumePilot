from io import BytesIO
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def generate_pdf(score, matched_skills, missing_skills,
                 recommendation, found_sections, missing_sections):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("<b>ResumePilot Analysis Report</b>", styles["Title"]))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph(f"<b>ATS Score:</b> {score}%", styles["Heading2"]))
    elements.append(Spacer(1, 15))

    # Matched Skills
    elements.append(Paragraph("<b>Matched Skills</b>", styles["Heading2"]))
    for skill in matched_skills:
        elements.append(Paragraph(f"• {skill}", styles["BodyText"]))

    elements.append(Spacer(1, 15))

    # Missing Skills
    elements.append(Paragraph("<b>Missing Skills</b>", styles["Heading2"]))
    for skill in missing_skills:
        elements.append(Paragraph(f"• {skill}", styles["BodyText"]))

    elements.append(Spacer(1, 15))

    # Resume Sections
    elements.append(Paragraph("<b>Resume Sections</b>", styles["Heading2"]))

    for section in found_sections:
        elements.append(Paragraph(f"✓ {section}", styles["BodyText"]))

    for section in missing_sections:
        elements.append(Paragraph(f"✗ {section}", styles["BodyText"]))

    elements.append(Spacer(1, 15))

    # Recommendation
    elements.append(Paragraph("<b>AI Recommendation</b>", styles["Heading2"]))
    elements.append(Paragraph(recommendation, styles["BodyText"]))

    doc.build(elements)

    buffer.seek(0)

    return buffer