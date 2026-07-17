from services.ai_service import get_ai_response


def analyze_sleep(hours, quality, bedtime, wake_time, feeling):

    prompt = f"""
You are an AI Sleep Health Assistant.

Analyze the following sleep information.

Hours slept: {hours}
Sleep quality (1-10): {quality}
Bedtime: {bedtime}
Wake-up time: {wake_time}
Morning feeling: {feeling}

Provide:

1. Overall Sleep Score (out of 10)
2. Sleep Quality Analysis
3. Possible reasons for poor/good sleep
4. Health impact
5. Personalized recommendations
6. One motivational sentence

Keep the response supportive and concise.
"""

    return get_ai_response(prompt)