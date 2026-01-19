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
