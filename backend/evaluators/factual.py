import json
import re
from services.gemini_service import generate_response
from utils.json_parser import parse_json

def evaluate_factual_accuracy(user_prompt, llm_response):

    evaluation_prompt = f"""
You are an expert AI evaluator.

Evaluate the factual accuracy of the following AI response.

User Prompt:
{user_prompt}

LLM Response:
{llm_response}

Return ONLY valid JSON.

Format:

{{
    "accuracy_score":0.0,
    "confidence":"HIGH",
    "reason":"..."
}}

Rules:

- accuracy_score must be between 0 and 1
- 1 = Completely factually correct
- 0 = Completely incorrect

Confidence values:
HIGH
MEDIUM
LOW

Return ONLY JSON.
"""

    result = generate_response(evaluation_prompt)
    result = result.replace("```json", "").replace("```", "").strip()

    try:
        return parse_json(result)

    except Exception:
        return {
            "accuracy_score": None,
            "confidence": "UNKNOWN",
            "reason": result
        }