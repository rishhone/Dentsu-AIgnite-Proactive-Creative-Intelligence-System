import numpy as np

def detect_fatigue(ctr_series):
    if len(ctr_series) < 2:
        return False
    slope = np.polyfit(range(len(ctr_series)), ctr_series, 1)[0]
    return slope < -0.002
