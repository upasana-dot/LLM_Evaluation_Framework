from datetime import datetime

from services.gemini_service import generate_response

from evaluators.bias import evaluate_bias
from evaluators.toxicity import evaluate_toxicity
from evaluators.safety import evaluate_safety
from evaluators.factual import evaluate_factual_accuracy
from evaluators.hallucination import evaluate_hallucination
from scoring.overall_score import calculate_overall_score


def evaluate_prompt(user_prompt):

    llm_response = generate_response(user_prompt)
    if llm_response == "ERROR: GEMINI_QUOTA_EXCEEDED":
        return {
            "error": "Gemini API quota exceeded. Please try again later."
        }
    bias_result = evaluate_bias(user_prompt, llm_response)
    toxicity_result = evaluate_toxicity(llm_response)
    safety_result = evaluate_safety(user_prompt, llm_response)
    factual_result = evaluate_factual_accuracy(user_prompt, llm_response)
    hallucination_result = evaluate_hallucination(user_prompt,llm_response
)

    report = {

        "timestamp": datetime.now().isoformat(),
        "prompt": user_prompt,
        "response": llm_response,
        "bias": bias_result,
        "toxicity": toxicity_result,
        "safety": safety_result,
        "factual_accuracy": factual_result,
        "hallucination": hallucination_result

    }
    overall = calculate_overall_score(report)

    report["overall"] = overall

    return report