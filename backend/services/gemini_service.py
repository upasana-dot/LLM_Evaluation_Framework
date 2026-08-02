from google import genai
from config import GEMINI_API_KEY, MODEL_NAME
from google.genai.errors import ClientError

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_response(prompt):
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        return response.text
    except ClientError as e:
        if "429" in str(e):
            return "Error: Gemini_Quota_exceeded"

        raise
