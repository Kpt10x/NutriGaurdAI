import os
import json
from dotenv import load_dotenv
from google import genai
from prompts import NUTRITION_SYSTEM_PROMPT

# Load environment variables
load_dotenv()

# Initialize client with API key
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def analyze_meal(meal_text: str) -> dict:
    if not meal_text.strip():
        raise ValueError("Meal input cannot be empty")

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=NUTRITION_SYSTEM_PROMPT + f"\nUser input: {meal_text}"
    )

    try:
        return json.loads(response.text)
    except Exception:
        raise ValueError("Gemini returned invalid JSON")