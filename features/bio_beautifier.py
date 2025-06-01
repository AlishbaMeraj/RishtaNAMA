import streamlit as st
from openrouter_api import generate_text

def show_bio_beautifier():
    st.subheader("🧕 Bio Beautifier")

    bio_input = st.text_area("Enter your current rishta bio (English or Urdu):", "")

    if st.button("Beautify My Bio"):
        if bio_input.strip() == "":
            st.warning("Please enter or paste your rishta bio.")
            return

        prompt = f"""
        You're a professional bio editor for matrimonial profiles.
        Enhance the following bio using a polite and graceful tone with a soft blend of Urdu and English.
        Make it emotionally appealing, respectful, and suitable for a serious yet friendly matrimonial impression:
        "{bio_input}"
        """

        try:
            with st.spinner("Refining your bio..."):
                result = generate_text(prompt).strip()

            st.success("Here’s your improved bio:")
            st.text_area("📋 You can copy and use this version:", value=result, height=100)

        except Exception as e:
            st.error("Something went wrong. Please try again later.")
