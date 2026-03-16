SKILLS_DB = [

    "python","java","django","flask","react","angular",

    "sql","mongodb","machine learning","deep learning",

    "data science","aws","docker","kubernetes",

    "javascript","html","css","git","rest api"

]


def extract_skills(resume_text):

    text = resume_text.lower()

    skills = []

    for skill in SKILLS_DB:

        if skill in text:

            skills.append(skill)

    return list(set(skills))