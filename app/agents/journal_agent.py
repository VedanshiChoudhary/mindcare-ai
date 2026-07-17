from services.ai_service import get_ai_response


def analyze_journal(user_message):

    prompt = f"""
You are a mental health journaling assistant.

Analyze the user's journal entry and provide:

1. A short summary of their thoughts
2. Possible emotions they are expressing
3. A helpful reflection question
4. One small positive action they can take

Journal entry:
{user_message}

Keep the response supportive and simple.
"""

    result = get_ai_response(prompt)

    return result