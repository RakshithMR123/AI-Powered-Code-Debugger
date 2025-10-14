import cohere
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Cohere client
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
if not COHERE_API_KEY:
    raise ValueError("COHERE_API_KEY not found in .env file.")

co = cohere.Client(COHERE_API_KEY)

def get_text_output(input_text):
    """
    Generate a response from Cohere's chat model for the given input text.
    """
    try:
        output = co.chat(
            model="command-r-08-2024",  # Updated model
            message=input_text
        )
        return output.text
    except Exception as e:
        # Catch all exceptions, including API errors
        return f"Error: {e}"
