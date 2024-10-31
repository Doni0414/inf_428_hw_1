import numpy as np

def calculate_threat_score(departments):
    total_importance = np.sum([department["importance"] for department in departments])
    weighted_total_score = np.sum([department["importance"] * np.mean(department["threat_scores"]) for department in departments])

    return weighted_total_score / total_importance
