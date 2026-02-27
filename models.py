from pydantic import BaseModel
from typing import Dict, List, Optional

class Candidate(BaseModel):
    id: int
    name: str
    skills: Dict[str, float]  # skill: proficiency (0-1)
    experience_years: float
    gender: Optional[str] = None   # ignored for fairness
    college: Optional[str] = None  # ignored

class Project(BaseModel):
    id: int
    title: str
    required_skills: Dict[str, float]  # skill: weight
    min_experience: float