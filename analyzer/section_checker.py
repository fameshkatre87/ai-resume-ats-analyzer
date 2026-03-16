import re


def check_sections(resume_text):

    text = resume_text.lower()

    sections = {

        "Contact Info": False,

        "Skills": False,

        "Experience": False,

        "Education": False,

        "Projects": False

    }

    if re.search(r'email|phone', text):

        sections["Contact Info"] = True

    if "skills" in text:

        sections["Skills"] = True

    if "experience" in text:

        sections["Experience"] = True

    if "education" in text:

        sections["Education"] = True

    if "project" in text:

        sections["Projects"] = True

    return sections