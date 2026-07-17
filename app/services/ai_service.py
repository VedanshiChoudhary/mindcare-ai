import ollama

def get_ai_response(user_message):

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    return response["message"]["content"]