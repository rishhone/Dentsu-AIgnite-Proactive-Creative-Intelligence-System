def encode_text(headline, cta):
    urgency_terms = ["now", "today", "limited"]
    return {
        "cta": cta,
        "urgency": sum(t in headline.lower() for t in urgency_terms),
        "text_length": len(headline)
    }
