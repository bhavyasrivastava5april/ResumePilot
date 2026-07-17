
import re
from utils.skills_db import SKILL_ALIASES


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill, aliases in SKILL_ALIASES.items():
        for alias in aliases:

            pattern = r'(?<!\w)' + re.escape(alias.lower()) + r'(?!\w)'

            if re.search(pattern, text):
                found_skills.append(skill)
                break

    return sorted(found_skills)