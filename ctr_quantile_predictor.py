import numpy as np

def predict_ctr_distribution(embedding):
    base = np.clip(np.mean(embedding), 0.4, 1.8)
    return {
        "p10": round(base * 0.7, 4),
        "p50": round(base * 1.0, 4),
        "p90": round(base * 1.4, 4)
    }
