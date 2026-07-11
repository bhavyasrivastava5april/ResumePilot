
from utils.skills_db import SKILLS
import re


def extract_skills(text):

    text = text.lower()

    words = set(re.findall(r"\b[\w.+#-]+\b", text))

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in words:
            found_skills.append(skill)

    return sorted(found_skills)