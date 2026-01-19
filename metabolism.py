# BMR/TDEE calculator
ACTIVITY_MULTIPLIERS = {
    "sedentary": 1.2,
    "light": 1.375,
    "moderate": 1.55,
    "very_active": 1.725
}

def calculate_bmr(age, weight_kg, height_cm, gender):
    if gender.lower() == "male":
        return 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        return 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

def calculate_tdee(bmr, activity_level):
    return bmr * ACTIVITY_MULTIPLIERS.get(activity_level, 1.55)

def calculate_target_calories(tdee, goal):
    if goal == "loss":
        return int(tdee - 500)
    if goal == "gain":
        return int(tdee + 500)
    return int(tdee)
