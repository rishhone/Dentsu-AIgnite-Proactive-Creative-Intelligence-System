def causal_attribution(features):
    effects = []
    if features["has_human"]:
        effects.append(("Human Presence", "+0.18%", "High"))
    if features["cta"] == "Shop Now":
        effects.append(("CTA 'Shop Now'", "+0.25%", "High"))
    return effects
