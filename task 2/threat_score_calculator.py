import numpy as np

def calculate_threat_score(data):
    return np.max([calculate_threat_score_helper(np.array(x)) for x in data])

def calculate_threat_score_helper(data):
    mean = np.mean(data)
    variance = np.var(data)

    if variance > 150:
        return np.mean(data[(data - mean)**2 >= variance])
    return mean