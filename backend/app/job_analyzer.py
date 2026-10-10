from app.skill_extractor import extract_skills


def analyze_job_description(job_description: str) -> dict:
    """
    Extract required skills from a job description.
    """

    if not job_description.strip():
        return {
            "skills": [],
            "skill_count": 0
        }

    skills = extract_skills(job_description)

    return {
        "skills": skills,
        "skill_count": len(skills)
    }