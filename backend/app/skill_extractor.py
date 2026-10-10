
import re

SKILLS = {
    # Programming languages
    "Python": ["python"],
    "Java": ["java"],
    "JavaScript": ["javascript", "js"],
    "C++": ["c++"],
    "C#": ["c#"],

    # Web development
    "HTML": ["html", "html5"],
    "CSS": ["css", "css3"],
    "React": ["react", "react.js", "reactjs"],
    "Next.js": ["next.js", "nextjs"],
    "Node.js": ["node.js", "nodejs"],
    "FastAPI": ["fastapi"],
    "Django": ["django"],
    "Flask": ["flask"],
    "REST API": ["rest api", "restful api", "rest apis"],
    "Full Stack Development": ["full stack", "full-stack"],

    # Databases
    "SQL": ["sql"],
    "MySQL": ["mysql"],
    "PostgreSQL": ["postgresql", "postgres"],
    "MongoDB": ["mongodb", "mongo"],

    # QA and software testing
    "Software Testing": ["software testing", "software test"],
    "Manual Testing": ["manual testing", "manual tester"],
    "Automation Testing": ["automation testing", "test automation"],
    "Selenium": ["selenium", "selenium webdriver"],
    "Playwright": ["playwright"],
    "Cypress": ["cypress"],
    "API Testing": ["api testing", "api test"],
    "Postman": ["postman"],
    "Jira": ["jira"],
    "Test Cases": ["test case", "test cases", "test scenario", "test scenarios"],
    "Bug Reporting": ["bug reporting", "bug report", "defect reporting"],
    "Bug Life Cycle": ["bug life cycle", "defect life cycle"],
    "Regression Testing": ["regression testing", "regression test"],
    "Smoke Testing": ["smoke testing"],
    "Integration Testing": ["integration testing"],
    "Unit Testing": ["unit testing"],
    "SDLC": ["sdlc", "software development life cycle"],
    "STLC": ["stlc", "software testing life cycle"],

    # Data and AI/ML
    "Artificial Intelligence": ["artificial intelligence"],
    "Machine Learning": ["machine learning"],
    "Data Science": ["data science"],
    "Data Analysis": ["data analysis", "data analytics"],
    "Pandas": ["pandas"],
    "NumPy": ["numpy"],
    "Scikit-learn": ["scikit-learn", "sklearn"],
    "Excel": ["excel", "microsoft excel"],

    # Tools and concepts
    "Git": ["git", "github"],
    "Docker": ["docker"],
    "Linux": ["linux"],
    "Agile": ["agile"],
    "Scrum": ["scrum"],
    "Communication": ["communication skills", "communication"],
    "Problem Solving": ["problem-solving", "problem solving"],
}


def extract_skills(text: str) -> list[str]:
    if not text:
        return []

    found_skills = set()

    for skill, keywords in SKILLS.items():
        for keyword in keywords:
            pattern = r"(?<!\w)" + re.escape(keyword) + r"(?!\w)"

            if re.search(pattern, text, flags=re.IGNORECASE):
                found_skills.add(skill)
                break

    return sorted(found_skills)
