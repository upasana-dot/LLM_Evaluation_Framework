import json
import re

    
def parse_json(text):
    if not text:
        return None
    
    match = re.search(r"```json\s*(.*?)\s*```", text, re.DOTALL)
    
    if match:
        text = match.group(1)
    try:
        return json.loads(text)
    except:
        return None
    
extract_json = parse_json