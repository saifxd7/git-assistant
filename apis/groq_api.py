from groq import Groq
import logging
from config.config import load_environment_variables


class GroqAPI:
    def __init__(self):
        self.api_key = load_environment_variables()
        self.client = Groq(api_key=self.api_key)

    def generate_commit_message(self, diff, model_name):

        try:
            resp = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"Generate a commit message for the following code changes: \n{diff} \n Use gitHub's recommended commit message guidelines"
                    }
                ],
                model=model_name
            )
            return resp.choices[0].message.content
        except Exception as e:
            if hasattr(e, 'response') and e.response.status_code == 401:
                logging.error(f"Failed to generate commit message: Invalid API Key. Please check your API key in the .env file.")
                return None
            else:
                logging.error(f"Failed to generate commit message: {e}")
                return None