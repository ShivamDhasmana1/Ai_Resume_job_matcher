technical_skills = [
    "python", "java", "c++", "javascript", "html", "css", "sql",
    "react", "node.js", "flask", "django", "fastapi",
    "git", "github", "docker", "aws", "tensorflow", "pandas", "numpy"
]

soft_skills = [
    "communication", "leadership", "teamwork", "problem solving",
    "adaptability", "creativity", "critical thinking", "time management"
]

analytical_skills = [
    "data analysis", "data visualization", "machine learning",
    "deep learning", "statistics", "excel", "power bi", "tableau"
]

def get_all_skills():
    return list(set(technical_skills + soft_skills + analytical_skills))
