# AI Resume ATS Analyzer

An AI-powered Resume ATS Analyzer and Resume Builder built with Django.
This project helps job seekers analyze their resumes, check ATS compatibility, and generate optimized resumes with actionable suggestions.

## Project Overview

AI Resume ATS Analyzer is a web application designed to evaluate resumes against modern Applicant Tracking Systems (ATS).
It analyzes resume content, extracts skills, compares them with job descriptions, and provides improvement suggestions.

The system also includes a Resume Builder that allows users to create professional resumes and download them as PDF.

## Key Features

• Resume ATS Score Calculation
• Resume Parsing and Text Extraction
• Skill Extraction from Resume
• Skill Matching with Job Description
• Keyword Density Analysis
• Missing Skills Identification
• Resume Improvement Suggestions
• Resume Builder with PDF Download
• Clean and Simple Web Interface

## Tech Stack

Backend:

* Python
* Django

Libraries:

* ReportLab (PDF generation)
* NLP-based text analysis modules

Frontend:

* HTML
* CSS
* Django Templates

Database:

* SQLite

## Project Structure

ai_resume_ats
│
├── ai_resume_ats (Django project settings)
├── analyzer (Main application logic)
│   ├── ats_score.py
│   ├── skill_extractor.py
│   ├── keyword_analyzer.py
│   ├── resume_parser.py
│   ├── suggestion_engine.py
│   └── views.py
│
├── templates
│   ├── home.html
│   ├── resume_builder.html
│   └── resume_preview.html
│
├── manage.py
├── requirements.txt

## Installation

Clone the repository

git clone https://github.com/fameshkatre87/ai-resume-ats-analyze.git

Navigate to the project directory

cd ai-resume-ats-analyze

Create virtual environment

python -m venv venv

Activate environment

Windows:
venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run the Django server

python manage.py runserver

Open in browser

http://127.0.0.1:8000/

## How It Works

1. Upload your resume.
2. Enter a job description (optional).
3. The system extracts resume content.
4. It analyzes keywords, skills, and sections.
5. ATS score is calculated.
6. Suggestions are generated to improve resume quality.

## Future Improvements

• Machine Learning based resume ranking
• Job recommendation system
• AI powered resume rewriting
• Modern UI dashboard

## Author

Famesh Katre
MCA Student – Kamla Nehru Mahavidyalaya

GitHub: https://github.com/fameshkatre87

## License

This project is for educational and learning purposes.
