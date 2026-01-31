import numpy as np

def fuse_features(image_feat, video_feat, text_feat):
    embedding = image_feat["embedding"]
    if video_feat:
        embedding = np.concatenate([embedding, video_feat["embedding"]])
    return {
        "creative_embedding": embedding,
        "interpretable": {
            "has_human": image_feat["has_human"],
            "cta": text_feat["cta"]
        }
    }
