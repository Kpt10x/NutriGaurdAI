# NutriGuard AI

**Context-Aware Nutrition Intelligence System**

NutriGuard AI is a hybrid AI + deterministic backend system that converts natural language health input into a scientifically grounded metabolic profile and prepares the foundation for personalized nutrition intelligence.

---

## 🚀 Project Vision

Traditional calorie tracking apps rely on rigid forms and static food databases.  
NutriGuard AI uses **conversational AI + deterministic health logic** to deliver:

- Low-friction onboarding  
- Explainable calorie targets  
- Context-aware nutrition intelligence  
- Safety-first architecture for healthcare use cases  

---

## 🧠 Architecture Overview

[ User Chat Input ]  
⬇  
[ Profile Extraction (LLM) ]  
⬇  
[ Profile Validation (Python) ]  
⬇  
[ Metabolic Engine ]  
⬇  
[ Nutrition AI (Gemini) ]  
⬇  
[ Rule Engine ]  
⬇  
[ Visualization & Feedback ]


## 📌 Phase 1 – Core Backend (Completed)

### Features
- Conversational profile capture  
- Deterministic metabolic engine  
- Mifflin-St Jeor BMR calculation  
- TDEE and daily calorie target computation  
- Clean separation between AI and health logic  

### Why This Matters
- No hallucinations in health decisions  
- Fully explainable and auditable logic  
- Production-ready backend foundation  

---

## 📦 Project Structure

NutriGuardAI/  
├── app.py            → Streamlit entry point  
├── metabolism.py     → BMR, TDEE, Target Calories  
├── guardrails.py     → Health rule engine (Phase 3)  
├── nutrition_api.py  → Gemini integration (Phase 2)  
├── prompts.py        → System prompts  
├── utils.py          → Validation & helpers  
├── requirements.txt  → Dependencies  
└── README.md         → Documentation  


## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
