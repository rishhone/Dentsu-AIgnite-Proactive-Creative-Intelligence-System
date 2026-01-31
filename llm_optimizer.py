def generate_llm_recommendations(causal_insights, max_recos=2):
    recos = []
    for element, lift, conf in causal_insights:
        if conf == "High":
            recos.append({
                "suggestion": f"Improve {element}",
                "reason": f"Causal lift of {lift}"
            })
    return recos[:max_recos]
