import os
import logging
from dotenv import load_dotenv
from config.logging_config import setup_logging

load_dotenv()
setup_logging()

def load_environment_variables():
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    if not GROQ_API_KEY:
        logging.error("GROQ_API_KEY is not set in the environment variables.")
        raise EnvironmentError("GROQ_API_KEY is not set in the environment variables.")
    return GROQ_API_KEY