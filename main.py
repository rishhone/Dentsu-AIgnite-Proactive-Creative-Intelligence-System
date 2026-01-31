import pandas as pd

from multimodal.image_encoder import encode_image
from multimodal.video_encoder import encode_video
from multimodal.text_encoder import encode_text
from multimodal.fusion import fuse_features

from prediction.ctr_quantile_predictor import predict_ctr_distribution
from causality.attribution import causal_attribution

from optimization.llm_optimizer import generate_llm_recommendations
from feedback.human_feedback import apply_human_feedback
from feedback.fatigue_model import detect_fatigue
from optimization.creative_generator import generate_new_creative

creatives = pd.read_csv("data/creatives.csv")
performance = pd.read_csv("data/performance_history.csv")

outputs = []

for _, row in creatives.iterrows():
    img = encode_image(row.creative_id)
    vid = encode_video(row.creative_id) if row.creative_type == "video" else None
    text = encode_text(row.headline, row.cta)

    fused = fuse_features(img, vid, text)
    ctr_pred = predict_ctr_distribution(fused["creative_embedding"])
    causal = causal_attribution(fused["interpretable"])

    recos = generate_llm_recommendations(causal)
    approved = apply_human_feedback(recos)

    ctr_hist = performance[performance.creative_id == row.creative_id]["ctr"].tolist()
    fatigue = detect_fatigue(ctr_hist)

    new_creative = generate_new_creative(approved) if fatigue and approved else None

    outputs.append({
        "creative_id": row.creative_id,
        "ctr_prediction": ctr_pred,
        "causal_insights": causal,
        "recommendations": recos,
        "fatigue_detected": fatigue,
        "new_creative": new_creative
    })

pd.DataFrame(outputs).to_json("outputs/final_results.json", indent=2)
print("AIgnite pipeline executed successfully.")
