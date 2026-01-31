import numpy as np

def encode_video(creative_id, frames=8):
    np.random.seed(abs(hash(creative_id)) % 2000)
    frame_embeddings = [np.random.normal(0, 1, 16) for _ in range(frames)]
    return {
        "motion_score": np.random.uniform(0.1, 1.0),
        "embedding": np.mean(frame_embeddings, axis=0)
    }
