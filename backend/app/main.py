from fastapi import FastAPI, UploadFile, File, HTTPException
from app.resume_parser import extract_text_from_pdf
from app.skill_extractor import extract_skills
from pydantic import BaseModel
from app.job_analyzer import analyze_job_description
from app.match_score import calculate_match_score
from app.career_recommender import generate_career_recommendations
from fastapi.middleware.cors import CORSMiddleware
from pypdf.errors import EmptyFileError

app = FastAPI(
    title="AI Career Copilot API",
    description="AI-powered Resume and Job Matching Platform",
    version="1.0.0"
)
class JobDescription(BaseModel):
    description: str

@app.get("/")
def home():
    return {
        "message": "AI Career Copilot API is running 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# 👇 YE WALA PART ADD KARNA HAI
@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file was selected."
        )

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    file_content = await file.read()

    if not file_content:
        raise HTTPException(
            status_code=400,
            detail="The uploaded PDF is empty."
        )

    try:
        extracted_text = extract_text_from_pdf(file_content)

    except EmptyFileError:
        raise HTTPException(
            status_code=400,
            detail="The uploaded PDF is empty or invalid."
        )

    if not extracted_text:
        raise HTTPException(
            status_code=400,
            detail="Could not extract text from this PDF."
        )

    skills = extract_skills(extracted_text)

    return {
        "filename": file.filename,
        "characters": len(extracted_text),
        "skills": skills,
        "resume_text": extracted_text
    }
@app.post("/analyze-job")
def analyze_job(job: JobDescription):

    result = analyze_job_description(job.description)

    return {
        "job_description": job.description,
        "required_skills": result["skills"],
        "skill_count": result["skill_count"]
    }
@app.post("/match-resume")
def match_resume(data: dict):

    resume_skills = data.get("resume_skills", [])
    job_skills = data.get("job_skills", [])

    result = calculate_match_score(
        resume_skills,
        job_skills
    )

    return result
@app.post("/career-recommendations")
def career_recommendations(data: dict):

    missing_skills = data.get("missing_skills", [])

    result = generate_career_recommendations(missing_skills)

    return result
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)