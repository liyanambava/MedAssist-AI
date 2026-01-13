import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

DEBUG = True

import streamlit as st

from vision.features import extract_visual_features
from llm.reasoning_agent import generate_explanation
from triage.rules import assess_risk
from triage.risk_assessment import get_risk_message
from triage.specialty import infer_specialty
from safety.guardrails import check_safety

st.set_page_config(page_title="MedAssist AI", layout="centered")

st.title("🏥 MedAssist AI")
st.caption("AI-assisted medical decision support (not a diagnosis)")

# --- Image upload ---
uploaded_file = st.file_uploader("Upload a medical image", type=["jpg", "png", "jpeg"])

# --- Location ---
st.subheader("Location (optional)")
city = st.text_input(
    "Enter your city to find nearby healthcare facilities",
    help="Used only to open Google Maps. Not stored."
)

# --- Symptoms ---
st.subheader("Symptoms")
age = st.number_input("Age", min_value=0, max_value=120)
pain = st.slider("Pain level", 0, 10, 0)
duration = st.number_input("Duration (days)", min_value=0)
fever = st.checkbox("Fever present")
notes = st.text_area("Additional notes")

# --- Safety check ---
if not check_safety(notes):
    st.error("This request cannot be processed safely. Please consult a medical professional.")
    st.stop()

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded image", use_column_width=True)

    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.read())

    features = extract_visual_features("temp.jpg")

    symptoms = {
        "age": age,
        "pain": pain,
        "duration_days": duration,
        "fever": fever,
        "notes": notes
    }

    if st.button("Analyze"):
        # --- Core AI analysis ---
        with st.spinner("Analyzing..."):
            risk = assess_risk(features, symptoms)
            explanation = generate_explanation(features, symptoms, risk)
            risk_msg = get_risk_message(risk)

        # --- Display results ---
        st.subheader("🔍 Visual Features")
        st.json(features)

        st.subheader("🧠 AI Explanation")
        st.markdown(explanation)

        st.subheader("⚠️ Risk Assessment")
        st.write(f"**Risk level:** {risk}")
        st.info(risk_msg)

        # --- Infer specialty ---
        specialty = infer_specialty(features, symptoms)
        st.write(f"**Suggested specialty:** {specialty}")

        st.warning(
            "This tool does NOT provide a medical diagnosis. "
            "It is for informational and decision-support purposes only."
        )

        # --- Specialty-based Google Maps link ---
        if risk in ["MEDIUM", "HIGH"] and city:
            st.subheader("🏥 Nearby Healthcare Facilities")

            maps_query = f"{specialty} clinic in {city}"
            maps_url = f"https://www.google.com/maps/search/{maps_query.replace(' ', '+')}"

            st.markdown(
                f"You may consider visiting a nearby **{specialty} clinic**.\n\n"
                f"[🔍 View {specialty} clinics near {city} on Google Maps]({maps_url})"
            )

            st.caption(
                "Clinic suggestions are based on general symptoms and visual cues, "
                "not a medical diagnosis. Location is not stored."
            )
