def calculate_match_score(resume_skills: list, job_skills: list) -> dict:
    """
    Compare resume skills with job-required skills
    and calculate the match percentage.
    """

    resume_set = set(skill.lower() for skill in resume_skills)
    job_set = set(skill.lower() for skill in job_skills)

    if not job_set:
        return {
            "match_percentage": 0,
            "matching_skills": [],
            "missing_skills": []
        }

    matching_skills = resume_set.intersection(job_set)
    missing_skills = job_set - resume_set

    match_percentage = round(
        (len(matching_skills) / len(job_set)) * 100,
        2
    )

    return {
        "match_percentage": match_percentage,
        "matching_skills": sorted(matching_skills),
        "missing_skills": sorted(missing_skills)
    }