from services.ai_service import get_ai_response
import json


def analyze_mood(user_message):

    prompt = f"""
You are a mental health mood analysis assistant.

Analyze the user's message.

Return ONLY valid JSON in this format:

{{
    "emotion": "main emotion",
    "intensity": "Low, Medium, or High",
    "suggestion": "short supportive suggestion"
}}

User message:
{user_message}
"""

    result = get_ai_response(prompt)

    try:
        return json.loads(result)

    except:
        return {
            "emotion": "Unknown",
            "intensity": "Unknown",
            "suggestion": result
        }