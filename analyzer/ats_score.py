from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re


def calculate_ats_score(resume_text, job_description):

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    score = round(similarity[0][0] * 100, 2)

    return score


def resume_quality_score(resume_text):

    score = 0

    text = resume_text.lower()

    if re.search(r'email', text):

        score += 20

    if re.search(r'phone|mobile', text):

        score += 20

    if "skills" in text:

        score += 20

    if "experience" in text:

        score += 20

    if "education" in text:

        score += 20

    return score