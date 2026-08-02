from evaluators.toxicity import evaluate_toxicity

text = "You are stupid and I hate you."

result = evaluate_toxicity(text)

print(result)