
LEARNING_RECOMMENDATIONS = {
    "python": "Practice functions, OOP, data structures, exception handling and small Python projects.",
    "java": "Learn OOP, collections, exception handling and build a small Java application.",
    "sql": "Practice SELECT queries, JOINs, GROUP BY, subqueries and database design.",
    "mysql": "Practice CRUD operations, joins, indexes and relational database design.",
    "manual testing": "Learn test planning, test scenarios, test cases, exploratory testing and test execution.",
    "software testing": "Study SDLC, STLC, functional testing, regression testing and defect life cycle.",
    "automation testing": "Learn automation frameworks, test scripts, assertions and test reporting.",
    "selenium": "Practice Selenium WebDriver, locators, waits, browser automation and test scripts.",
    "playwright": "Learn browser automation, locators, assertions, fixtures and end-to-end testing.",
    "cypress": "Practice Cypress commands, assertions, fixtures and web application testing.",
    "api testing": "Learn HTTP methods, status codes, headers, request bodies and API validation.",
    "postman": "Practice GET, POST, PUT and DELETE requests, collections, environments and test scripts.",
    "jira": "Learn how to create issues, report bugs, manage workflows and track sprint tasks in Jira.",
    "test cases": "Write test cases with preconditions, test steps, test data, expected results and actual results.",
    "bug reporting": "Practice writing reproducible bug reports with severity, priority, steps, evidence and expected versus actual results.",
    "bug life cycle": "Study defect states, triage, assignment, fixing, retesting, verification and closure.",
    "regression testing": "Practice regression test selection and rerun tests after code changes.",
    "smoke testing": "Learn how to design a small test suite that checks critical application functionality.",
    "integration testing": "Practice testing interactions between modules, APIs and connected services.",
    "unit testing": "Learn unit test structure, assertions, mocks and test coverage.",
    "sdlc": "Study requirements, design, development, testing, deployment and maintenance phases.",
    "stlc": "Study test requirement analysis, planning, test design, execution and test closure.",
    "html": "Practice semantic HTML, forms, accessibility and page structure.",
    "css": "Build responsive layouts using Flexbox, Grid and media queries.",
    "javascript": "Practice ES6+, functions, arrays, promises, async/await and API integration.",
    "react": "Build components and practice hooks, state management and API integration.",
    "fastapi": "Build REST endpoints using FastAPI, Pydantic validation and error handling.",
    "git": "Practice commits, branches, merging, pull requests and resolving conflicts.",
    "communication": "Practice explaining technical issues clearly, writing concise updates and collaborating with teammates.",
    "problem solving": "Practice breaking problems into smaller steps and solving coding and debugging exercises.",
    "machine learning": "Study supervised learning, data preparation, model evaluation and scikit-learn projects.",
    "data analysis": "Practice cleaning datasets, exploratory analysis, visualization and communicating insights."
}


def generate_career_recommendations(missing_skills: list) -> dict:
    """
    Generate learning recommendations for missing job skills.
    """

    recommendations = []

    for skill in missing_skills:
        skill_lower = skill.lower().strip()

        recommendation = LEARNING_RECOMMENDATIONS.get(
            skill_lower,
            f"Study the fundamentals of {skill}, practice with hands-on exercises, and build a small project."
        )

        recommendations.append({
            "skill": skill,
            "recommendation": recommendation
        })

    return {
        "skill_gap_count": len(missing_skills),
        "recommendations": recommendations
    }
