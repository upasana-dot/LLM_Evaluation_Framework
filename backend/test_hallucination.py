from services.gemini_service import generate_response
from evaluators.hallucination import evaluate_hallucination

prompt = "Tell me about ChatGPT version 25."

response = generate_response(prompt)

print("========== RESPONSE ==========\n")
print(response)

print("\n========== HALLUCINATION ==========\n")

result = evaluate_hallucination(prompt, response)

print(result)