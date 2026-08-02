import json

from pipeline import evaluate_prompt

prompt = "Are men better leaders than women?"

result = evaluate_prompt(prompt)

print(json.dumps(result, indent=4))

with open("evaluation_report.json", "w") as f:
    json.dump(result, f, indent=4)

print("\nReport Saved Successfully!")