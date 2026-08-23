from sqlmodel import SQLModel, Field


class Candidate(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    name: str
    email: str | None = None

    resume_text: str

    skills: str
    experience: str
    education: str

    match_score: float | None = None
    matching_skills: str | None = None
    missing_skills: str | None = None
    justification: str | None = None
