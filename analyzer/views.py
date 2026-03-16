
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas

from .ai_improver import improve_resume
from .forms import ResumeForm
from .resume_parser import extract_resume_text
from .ats_score import calculate_ats_score, resume_quality_score
from .skill_extractor import extract_skills
from .skill_matcher import match_skills
from .section_checker import check_sections
from .keyword_analyzer import keyword_density
from .suggestion_engine import generate_suggestions
from .resume_builder_forms import ResumeBuilderForm



def resume_builder(request):

    form = ResumeBuilderForm()

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        github = request.POST.get("github")
        linkedin = request.POST.get("linkedin")
        objective = request.POST.get("objective")

        skills = request.POST.getlist("skills[]")

        company = request.POST.getlist("company[]")
        role = request.POST.getlist("role[]")
        duration = request.POST.getlist("duration[]")
        experience_detail = request.POST.getlist("experience_detail[]")

        college = request.POST.getlist("college_name[]")
        degree = request.POST.getlist("degree[]")
        year = request.POST.getlist("year[]")
        percentage = request.POST.getlist("percentage[]")

        project_name = request.POST.getlist("project_name[]")
        project_detail = request.POST.getlist("project_detail[]")
        project_link = request.POST.getlist("project_link[]")

        certificates = request.POST.getlist("certificates[]")
        achievements = request.POST.getlist("achievements[]")

        languages = request.POST.getlist("languages[]")
        interests = request.POST.getlist("interests[]")
        links = request.POST.getlist("links[]")

        education = list(zip(college, degree, year, percentage))
        projects = list(zip(project_name, project_detail, project_link))
        experience = list(zip(company, role, duration, experience_detail))

        # AI Resume Improve
        resume_text = " ".join(skills) + " " + (objective or "")
        ai_suggestions, rewrites = improve_resume(resume_text)

        context = {
            "name": name,
            "email": email,
            "phone": phone,
            "github": github,
            "linkedin": linkedin,
            "objective": objective,
            "skills": skills,
            "experience": experience,
            "education": education,
            "projects": projects,
            "certificates": certificates,
            "achievements": achievements,
            "languages": languages,
            "interests": interests,
            "links": links,
            "ai_suggestions": ai_suggestions,
            "rewrites": rewrites
        }

        if "preview" in request.POST:
            return render(request, "resume_preview.html", context)

        # -------- Download PDF --------

        if "download" in request.POST:

            response = HttpResponse(content_type="application/pdf")
            response["Content-Disposition"] = 'attachment; filename="resume.pdf"'

            p = canvas.Canvas(response)

            text = p.beginText(50, 800)
            text.setFont("Helvetica", 11)
            text.setLeading(16)

            text.setFont("Helvetica-Bold", 16)
            text.textLine(name)

            text.setFont("Helvetica", 11)

            contact = f"{email} | {phone}"

            if linkedin:
                contact += f" | {linkedin}"

            if github:
                contact += f" | {github}"

            text.textLine(contact)
            text.textLine("")

            if objective:
                text.setFont("Helvetica-Bold", 13)
                text.textLine("OBJECTIVE")
                text.setFont("Helvetica", 11)
                text.textLine(objective)
                text.textLine("")

            if skills:
                text.setFont("Helvetica-Bold", 13)
                text.textLine("SKILLS")

                for s in skills:
                    if s:
                        text.textLine(f"• {s}")

                text.textLine("")

            if experience:
                text.setFont("Helvetica-Bold", 13)
                text.textLine("EXPERIENCE")

                for c, r, d, desc in experience:

                    if not c and not r and not desc:
                        continue

                    if r:
                        text.setFont("Helvetica-Bold", 11)
                        text.textLine(r)

                    text.setFont("Helvetica", 11)

                    if c:
                        text.textLine(c)

                    if d:
                        text.textLine(d)

                    if desc:
                        text.textLine(desc)

                    text.textLine("")

            if education:
                text.setFont("Helvetica-Bold", 13)
                text.textLine("EDUCATION")

                for c, d, y, pct in education:

                    if c:
                        text.textLine(c)

                    if d:
                        text.textLine(f"{d} - {y}")

                    if pct:
                        text.textLine(f"CGPA: {pct}")

                    text.textLine("")

            if projects:
                text.setFont("Helvetica-Bold", 13)
                text.textLine("PROJECTS")

                for n, d, l in projects:

                    if not n and not d and not l:
                        continue

                    if n:
                        text.setFont("Helvetica-Bold", 11)
                        text.textLine(n)

                    text.setFont("Helvetica", 11)

                    if d:
                        text.textLine(d)

                    if l:
                        text.textLine(l)

                    text.textLine("")

            if certificates:
                text.setFont("Helvetica-Bold", 13)
                text.textLine("CERTIFICATES")

                for c in certificates:
                    if c:
                        text.textLine(f"• {c}")

                text.textLine("")

            if achievements:
                text.setFont("Helvetica-Bold", 13)
                text.textLine("ACHIEVEMENTS")

                for a in achievements:
                    if a:
                        text.textLine(f"• {a}")

                text.textLine("")

            p.drawText(text)
            p.save()

            return response

    return render(request, "resume_builder.html", {"form": form})



# resume 

def home(request):

    score = None
    skills = None
    matched = []
    missing = []
    sections = None
    keywords = None
    suggestions = None
    ai_suggestions = []
    rewrites = []
    match_percent = 0
    strength = ""

    if request.method == "POST":

        form = ResumeForm(request.POST, request.FILES)

        if form.is_valid():

            resume_file = request.FILES["resume"]
            job_description = form.cleaned_data["job_description"]

            resume_text = extract_resume_text(resume_file)

            skills = extract_skills(resume_text)
            sections = check_sections(resume_text)
            keywords = keyword_density(resume_text)

            if job_description.strip() == "":
                score = resume_quality_score(resume_text)

            else:
                score = calculate_ats_score(resume_text, job_description)
                matched, missing = match_skills(skills, job_description)

            suggestions = generate_suggestions(missing, sections, score)

            # AI Improve
            ai_suggestions, rewrites = improve_resume(resume_text)

            # Job Match %
            total = len(matched) + len(missing)

            if total > 0:
                match_percent = int((len(matched) / total) * 100)

            # Resume Strength
            if score:

                if score < 50:
                    strength = "Weak Resume"

                elif score < 75:
                    strength = "Average Resume"

                else:
                    strength = "Strong Resume"

    else:
        form = ResumeForm()

    return render(request, "home.html", {
        "form": form,
        "score": score,
        "skills": skills,
        "matched": matched,
        "missing": missing,
        "sections": sections,
        "keywords": keywords,
        "suggestions": suggestions,
        "ai_suggestions": ai_suggestions,
        "rewrites": rewrites,
        "match_percent": match_percent,
        "strength": strength
    })
