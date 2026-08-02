from services.gemini_service import generate_response
from evaluators.factual import evaluate_factual_accuracy

prompt = "Who invented the telephone?"

response = generate_response(prompt)

print("========== RESPONSE ==========\n")
print(response)

print("\n========== FACTUAL EVALUATION ==========\n")

result = evaluate_factual_accuracy(prompt, response)

print(result)