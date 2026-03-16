from collections import Counter


def keyword_density(resume_text):

    words = resume_text.lower().split()

    counter = Counter(words)

    keywords = [

        "python","django","sql",

        "machine","learning","aws",

        "docker","react"

    ]

    result = {}

    for word in keywords:

        result[word] = counter[word]

    return result