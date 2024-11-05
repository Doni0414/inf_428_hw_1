import numpy as np

def time_to_cyclic(hour):
    """Converts a given hour (0-23) into cyclic sine and cosine features."""
    radians = 2 * np.pi * (hour ) / 24
    return np.sin(radians), np.cos(radians)

def validate_hour(hour):
    if hour < 0 or hour >= 24:
        raise Exception(f"hour should be in [0,23] interval! Actual: {hour}")
    
def time_difference_simple(hour1, hour2):
    validate_hour(hour1)
    validate_hour(hour2)

    return (hour2 - hour1) % 24

def time_difference_trigonometry(hour1, hour2):
    validate_hour(hour1)
    validate_hour(hour2)

    sin1, cos1 = time_to_cyclic(hour1)
    sin2, cos2 = time_to_cyclic(hour2)
    
    angle_diff = np.arctan2(sin2, cos2) - np.arctan2(sin1, cos1)
    
    hour_diff = (angle_diff * 24) / (2 * np.pi)
    return np.abs(hour_diff)

print(time_difference_trigonometry(1,23))