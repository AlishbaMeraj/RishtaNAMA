import streamlit as st
from openrouter_api import generate_text

def show_pickup_lines():
    st.header("🎯 Cute Pickup Lines Banaiye")

    mood = st.selectbox("Apka mood kya hai?", ["Romantic", "Funny", "Nerdy"])
    gender = st.radio("Select your intention:", ["Impress me", "I want to impress someone"])

    if st.button("Line Generate Karo 💘"):
        prompt = f"""Generate a {mood.lower()} Urdu-English pickup line for rishta context. 
        Gender context: {"for a girl" if gender == "Impress me" else "for a boy"}.
        The line should be classy, cute, and 1-2 lines only."""

        try:
            with st.spinner("Generating line... 💌"):
                response = generate_text(prompt)
                pickup_line = response.strip()

            st.success("Mission rishta initiated — line tayyar hai 💡😉")
            st.markdown(f"🌟 **{pickup_line}**")
            st.text_area("📋 Isay copy karo aur bhej do!", value=pickup_line, height=100)

            if st.button("🔁 Nai Line Try Karo"):
                st.rerun()

        except Exception as e:
            st.error("Kuch error aa gaya. Please try again later.")
