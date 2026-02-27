from fastapi import FastAPI # Fixed: 'From' changed to 'from'
from typing import List
from models import Candidate, Project
from matcher import (
    normalize_skills,
    compute_weighted_score,
    apply_experience_filter,
    fairness_adjustment,
    generate_explanation
)

app = FastAPI(title="Explainable Skill-Based Matching Platform")

@app.post("/match/")
def match_candidates(project: Project, candidates: List[Candidate]):

    ranked_list = []

    for candidate in candidates:
        # Fixed: Renamed variable to 'norm_skills' to avoid 
        # overwriting the imported function 'normalize_skills'
        norm_skills = normalize_skills(candidate.skills)

        score, contributions = compute_weighted_score(
            norm_skills,
            project.required_skills
        )

        score = apply_experience_filter(
            score,
            candidate.experience_years,
            project.min_experience
        )

        explanation = generate_explanation(
            candidate,
            project,
            score,
            contributions
        )

        ranked_list.append({
            "candidate_id": candidate.id,
            "name": candidate.name,
            "score": score,
            "explanation": explanation
        })

    final_ranking = fairness_adjustment(ranked_list)

    return {
        "project": project.title,
        "ranking": final_ranking
    }