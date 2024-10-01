import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
# Get the API key from the environment variable
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

BOT_NAME="Bob"
MODEL_NAME="gpt-4o-mini"
MAX_LIMIT_INPUT=100
LLM_TEMPERATURE=0