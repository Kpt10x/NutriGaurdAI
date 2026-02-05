#streamline entry point
import streamlit as st
from metabolism import calculate_bmr, calculate_tdee, calculate_target_calories
from utils import validate_profile

st.title("NutriGuard AI")

if "profile" not in st.session_state:
    st.session_state.profile = {
        "age": None, "height_cm": None, "weight_kg": None,
        "gender": None, "activity_level": None, "goal": None
    }

msg = st.text_input("Tell me about yourself (age, height, weight, activity, goal)")

if msg:
    import re
    if "year" in msg:
        st.session_state.profile["age"] = int(re.findall(r"\d+", msg)[0])
    if "cm" in msg:
        st.session_state.profile["height_cm"] = int(re.findall(r"\d+ cm", msg)[0].split()[0])
    if "kg" in msg:
        st.session_state.profile["weight_kg"] = int(re.findall(r"\d+ kg", msg)[0].split()[0])
    if "male" in msg.lower():
        st.session_state.profile["gender"] = "male"
    if "female" in msg.lower():
        st.session_state.profile["gender"] = "female"
    if "sedentary" in msg.lower():
        st.session_state.profile["activity_level"] = "sedentary"
    if "lose" in msg.lower():
        st.session_state.profile["goal"] = "loss"

missing = validate_profile(st.session_state.profile)

if not missing:
    p = st.session_state.profile
    bmr = calculate_bmr(p["age"], p["weight_kg"], p["height_cm"], p["gender"])
    tdee = calculate_tdee(bmr, p["activity_level"])
    target = calculate_target_calories(tdee, p["goal"])

    st.success("Profile Completed")
    st.metric("BMR", round(bmr, 1))
    st.metric("TDEE", round(tdee, 1))
    st.metric("Target Calories", target)
else:
    st.info(f"Missing fields: {missing}")

st.divider()
st.header("Meal Analysis (Phase 2)")

meal = st.text_input("What did you eat today?")

if st.button("Analyze Meal"):
    from nutrition_api import analyze_meal
    from utils import validate_nutrition_json

    try:
        nutrition = analyze_meal(meal)

        if validate_nutrition_json(nutrition):
            st.success("Meal analyzed successfully")
            st.json(nutrition["total"])
        else:
            st.error("Invalid nutrition data format")

    except Exception as e:
        st.error(str(e))
