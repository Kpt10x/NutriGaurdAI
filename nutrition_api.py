import json
import google.generativeai as genai
from prompts import NUTRITION_SYSTEM_PROMPT

def analyze_meal(meal_text: str) -> dict:
    """
    Sends meal text to Gemini and returns structured nutrition JSON.
    AI is constrained to estimation only.
    """

    if not meal_text or len(meal_text.strip()) == 0:
        raise ValueError("Meal input cannot be empty")

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(
        NUTRITION_SYSTEM_PROMPT + f"\nUser input: {meal_text}"
    )

    try:
        data = json.loads(response.text)
    except Exception:
        raise ValueError("Gemini returned invalid JSON")

    return data
