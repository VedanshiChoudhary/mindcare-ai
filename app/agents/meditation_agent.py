from services.ai_service import get_ai_response


def suggest_meditation(emotion, intensity):

    prompt = f"""
You are an AI meditation assistant.

The user's current emotion:
{emotion}

Emotional intensity:
{intensity}

Suggest a suitable meditation practice.

Include:
1. Meditation name
2. Duration
3. Simple steps
4. Benefits

Keep the response supportive and concise.
"""

    return get_ai_response(prompt)