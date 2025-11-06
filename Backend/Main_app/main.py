from fastapi import FastAPI, File, UploadFile
import PyPDF2
import docx
import os

from Main_app.clean_text_module import clean_text
from Main_app.extract_skills import extract_skills_from_text
from Main_app.job_database import jobs
from Main_app.ai_matcher import ai_match_jobs
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Resume & Job Matcher is running 🚀"}

@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    filename = file.filename

    # Check file type
    if not (filename.endswith(".pdf") or filename.endswith(".docx")):
        return {"error": "Only PDF or DOCX files are supported."}

    # Save uploaded file temporarily
    temp_path = f"temp_{filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    # Extract text
    text = ""
    if filename.endswith(".pdf"):
        with open(temp_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                text += page.extract_text() or ""
    else:
        doc = docx.Document(temp_path)
        text = "\n".join([p.text for p in doc.paragraphs])

    # Clean the resume text
    cleaned_output = clean_text(text)
    cleaned_text = cleaned_output["cleaned_text"]

    # Extract skills
    skills = extract_skills_from_text(cleaned_text)

    # AI Job Matching
    ai_matches = ai_match_jobs(cleaned_text, jobs)

    # Save outputs
    with open("myfile.txt", "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    with open("ai_job_matches.txt", "w", encoding="utf-8") as f:
        for match in ai_matches:
            f.write(f"{match['job_title']} ({match['company']}) - {match['match_score']}%\n")

    os.remove(temp_path)

    return {
        "message": "Resume processed and AI job matches found",
        "emails": cleaned_output["emails"],
        "phones": cleaned_output["phones"],
        "urls": cleaned_output["urls"],
        "skills": skills,
        "ai_job_matches": ai_matches
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/analyze-resume/")
async def analyze_resume(data: dict):
    # Your AI analysis logic here
    insights = [
        {
            "category": "Grammar & Clarity",
            "suggestions": ["Use active voice", "Fix typos in experience section"],
            "priority": "high"
        }
    ]
    return {"insights": insights}
