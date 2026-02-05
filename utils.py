# Helpers & Validators
def validate_profile(profile):
    required = ["age", "height_cm", "weight_kg", "gender", "activity_level", "goal"]
    missing = [k for k in required if profile.get(k) is None]
    return missing

def normalize_activity(text):
    text = text.lower()
    if "sedentary" in text or "sitting" in text:
        return "sedentary"
    if "light" in text or "walking" in text:
        return "light"
    if "moderate" in text:
        return "moderate"
    if "very" in text or "intense" in text:
        return "very_active"
    return "moderate"

def validate_nutrition_json(data: dict) -> bool:
    """
    Ensures AI output follows required nutrition schema.
    """

    if not isinstance(data, dict):
        return False

    if "food_items" not in data or "total" not in data:
        return False

    if not isinstance(data["food_items"], list):
        return False

    required_item_keys = {
        "name", "calories", "protein", "carbs",
        "fats", "fiber", "sugar", "sodium"
    }

    for item in data["food_items"]:
        if not required_item_keys.issubset(item.keys()):
            return False

    required_total_keys = {
        "calories", "protein", "carbs",
        "fats", "sugar", "sodium"
    }

    if not required_total_keys.issubset(data["total"].keys()):
        return False

    return True
