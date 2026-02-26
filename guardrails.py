# Health rule Engine
def run_guardrails(profile: dict, nutrition: dict) -> list:
    """
    Evaluates nutrition totals against user health conditions.
    Returns a list of human-readable alerts.
    """

    alerts = []
    condition = profile.get("health_condition", "").lower()
    totals = nutrition.get("total", {})

    sugar = totals.get("sugar", 0)
    sodium = totals.get("sodium", 0)
    protein = totals.get("protein", 0)

    if condition == "diabetes":
        if sugar > 25:
            alerts.append(
                "⚠️ Sugar Spike Warning: This meal exceeds safe sugar limits for diabetes."
            )

    if condition in ["hypertension", "high bp", "bp"]:
        if sodium > 500:
            alerts.append(
                "⚠️ High Sodium Warning: This meal may increase blood pressure."
            )

    if condition in ["kidney", "kidney issues", "renal"]:
        if protein > 30:
            alerts.append(
                "⚠️ Protein Limit Exceeded: High protein intake may stress kidneys."
            )

    return alerts