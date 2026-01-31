import numpy as np

def encode_image(creative_id):
    np.random.seed(abs(hash(creative_id)) % 1000)
    return {
        "brightness": np.random.uniform(0.3, 0.8),
        "color_entropy": np.random.uniform(0.2, 0.9),
        "has_human": np.random.choice([0, 1]),
        "embedding": np.random.normal(0, 1, 16)
    }
