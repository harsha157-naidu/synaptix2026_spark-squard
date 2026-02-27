import numpy as np

FAIRNESS_THRESHOLD = 0.03  # 3% fairness margin


def normalize_skills(skills: dict):
    """
    Ensure all skill scores are between 0 and 1
    """
    return {k.lower(): min(max(v, 0), 1) for k, v in skills.items()}


def compute_weighted_score(candidate_skills, project_skills):
    """
    Compute weighted competency score
    """
    score = 0
    contribution = {}

    for skill, weight in project_skills.items():
        skill = skill.lower()
        candidate_value = candidate_skills.get(skill, 0)
        partial_score = candidate_value * weight
        contribution[skill] = round(partial_score, 3)
        score += partial_score

    return round(score, 3), contribution


def apply_experience_filter(score, candidate_exp, required_exp):
    """
    Penalize if experience is less than required
    """
    if candidate_exp < required_exp:
        penalty = 0.1  # 10% penalty
        score = score * (1 - penalty)
    return round(score, 3)


def fairness_adjustment(ranked_candidates):
    """
    Apply fairness-aware adjustment:
    If two candidates differ by less than threshold,
    keep original order (no demographic bias used).
    """
    adjusted = sorted(ranked_candidates, key=lambda x: x["score"], reverse=True)

    for i in range(len(adjusted) - 1):
        diff = abs(adjusted[i]["score"] - adjusted[i+1]["score"])
        if diff < FAIRNESS_THRESHOLD:
            # Keep stable ordering (no bias-based swap)
            continue

    return adjusted


def generate_explanation(candidate, project, score, contributions):
    explanation = {
        "candidate": candidate.name,
        "project": project.title,
        "match_score": score,
        "reasoning": []
    }

    for skill, value in contributions.items():
        explanation["reasoning"].append(
            f"{skill} contributed {round(value*100,2)}% to final score"
        )

    if candidate.experience_years < project.min_experience:
        explanation["reasoning"].append(
            "Experience penalty applied due to lower experience"
        )

    return explanation