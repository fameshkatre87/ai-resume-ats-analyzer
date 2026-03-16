def improve_resume(text):

    suggestions = []
    rewrites = []

    text = text.lower()

    if "created" in text:
        suggestions.append("Use stronger action verbs like Developed, Designed, Implemented.")
        rewrites.append("Developed and implemented a scalable web application using modern technologies.")

    if "project" in text:
        suggestions.append("Mention technologies used in the project.")
        rewrites.append("Built an AI-powered project using Python, Machine Learning, and data analysis.")

    if len(text.split()) < 20:
        suggestions.append("Add measurable achievements and results.")

    return suggestions, rewrites