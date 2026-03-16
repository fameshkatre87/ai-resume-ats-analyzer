from .skill_extractor import SKILLS_DB


def match_skills(resume_skills, job_description):

    job_description = job_description.lower()

    job_skills = []

    for skill in SKILLS_DB:

        if skill in job_description:

            job_skills.append(skill)

    matched = []

    missing = []

    for skill in job_skills:

        if skill in resume_skills:

            matched.append(skill)

        else:

            missing.append(skill)

    return matched, missing