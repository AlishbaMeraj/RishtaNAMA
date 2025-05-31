import streamlit as st
from openrouter_api import generate_text

def show_bio_beautifier():
    st.subheader("🧕 Bio Beautifier")
    bio_input = st.text_area("Paste your current rishta bio (English or Urdu):", "")

    if st.button("Beautify Bio"):
        if bio_input.strip() == "":
            st.warning("Please paste your rishta bio first.")
            return

        prompt = f"""
        Improve and beautify this rishta bio using poetic Urdu + soft English mix.
        Make it respectful, heartfelt, and suitable for a matrimonial profile:
        "{bio_input}"
        """

        try:
            with st.spinner("Beautifying your bio... ✨"):
                result = generate_text(prompt)
            st.success("Here's your new bio:")
            st.write(result)

        except Exception as e:
            st.error("Oops! Something went wrong while generating the bio.")
