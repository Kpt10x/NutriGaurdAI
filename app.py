import streamlit as st
from metabolism import calculate_bmr, calculate_tdee, calculate_target_calories
from utils import validate_profile, validate_nutrition_json
from nutrition_api import analyze_meal
from guardrails import run_guardrails


# ---------------------------------------------------
# App Config
# ---------------------------------------------------
st.set_page_config(page_title="NutriGuard AI", layout="centered")
st.title("NutriGuard AI")
st.caption("Context-Aware Nutrition Intelligence System")


# ---------------------------------------------------
# Session State Initialization
# ---------------------------------------------------
if "profile" not in st.session_state:
    st.session_state.profile = {
        "age": None,
        "height_cm": None,
        "weight_kg": None,
        "gender": None,
        "activity_level": None,
        "goal": None,
        "health_condition": "None"
    }

if "nutrition_data" not in st.session_state:
    st.session_state.nutrition_data = None


# ---------------------------------------------------
# PHASE 1 – Profile Intake & Metabolic Engine
# ---------------------------------------------------
st.header("Phase 1 – Metabolic Profile")

with st.expander("Enter Your Details"):
    age = st.number_input("Age", min_value=1, max_value=100, step=1)
    height = st.number_input("Height (cm)", min_value=50, max_value=250)
    weight = st.number_input("Weight (kg)", min_value=20, max_value=200)
    gender = st.selectbox("Gender", ["Male", "Female"])
    activity = st.selectbox(
        "Activity Level",
        ["sedentary", "light", "moderate", "very_active"]
    )
    goal = st.selectbox("Goal", ["loss", "maintenance", "gain"])
    condition = st.selectbox(
        "Health Condition",
        ["None", "Diabetes", "Hypertension", "Kidney"]
    )

    if st.button("Save Profile"):
        st.session_state.profile.update({
            "age": age,
            "height_cm": height,
            "weight_kg": weight,
            "gender": gender.lower(),
            "activity_level": activity,
            "goal": goal,
            "health_condition": condition
        })
        st.success("Profile Saved")


profile = st.session_state.profile

missing_fields = validate_profile(profile)

if not missing_fields:
    bmr = calculate_bmr(
        profile["age"],
        profile["weight_kg"],
        profile["height_cm"],
        profile["gender"]
    )
    tdee = calculate_tdee(bmr, profile["activity_level"])
    target = calculate_target_calories(tdee, profile["goal"])

    st.metric("BMR", round(bmr, 2))
    st.metric("TDEE", round(tdee, 2))
    st.metric("Target Calories", target)

    st.session_state.profile["target_calories"] = target

else:
    st.info(f"Missing fields: {missing_fields}")


# ---------------------------------------------------
# PHASE 2 – Meal Analysis (Gemini)
# ---------------------------------------------------
st.divider()
st.header("Phase 2 – Meal Analysis")

meal_text = st.text_input("What did you eat?")

if st.button("Analyze Meal"):
    try:
        nutrition_data = analyze_meal(meal_text)

        if validate_nutrition_json(nutrition_data):
            st.session_state.nutrition_data = nutrition_data
            st.success("Meal analyzed successfully")
            st.json(nutrition_data["total"])
        else:
            st.error("Invalid nutrition data structure")

    except Exception as e:
        st.error(str(e))


# ---------------------------------------------------
# PHASE 3 – Health Guardrails
# ---------------------------------------------------
st.divider()
st.header("Phase 3 – Health Guardrails")

if st.button("Check Health Impact"):

    if st.session_state.nutrition_data is None:
        st.warning("Please analyze a meal first.")
    else:
        alerts = run_guardrails(
            st.session_state.profile,
            st.session_state.nutrition_data
        )

        if alerts:
            for alert in alerts:
                st.error(alert)
        else:
            st.success("No health risks detected for this meal.")