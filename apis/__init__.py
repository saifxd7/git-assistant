import os
from groq import Groq

def get_groq_client():
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    if not GROQ_API_KEY:
        raise EnvironmentError("GROQ_API_KEY is not set in the environment variables.")
    return Groq(api_key=GROQ_API_KEY)

def generate_commit_message(diff, model_name):
    client = get_groq_client()
    resp = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Generate a commit message for the following code changes: \n{diff} \n Use gitHub's recommended commit message guidelines"
            }
        ],
        model=model_name
    )
    return resp.choices[0].message.content