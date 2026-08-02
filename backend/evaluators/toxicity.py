from detoxify import Detoxify


model = Detoxify("original")


def evaluate_toxicity(text):

    scores = model.predict(text)

    toxicity_score = scores["toxicity"]

    if toxicity_score < 0.30:
        risk = "LOW"

    elif toxicity_score < 0.70:
        risk = "MEDIUM"

    else:
        risk = "HIGH"

    return {
        "toxicity_score": round(float(toxicity_score), 3),
        "risk_level": risk
    }