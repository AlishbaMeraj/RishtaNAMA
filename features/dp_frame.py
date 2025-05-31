# features/dp_frame.py

import streamlit as st
from openrouter_api import generate_text

def show_dp_frame():
    st.subheader("📸 Rishta DP Frame Generator")
    # Future: User uploads image + selects theme
    theme = st.text_input("Describe your DP vibe (e.g., classy, cute, desi swag):")
    
    if st.button("Suggest Frame & Caption"):
        prompt = f"Suggest a poetic desi-style selfie frame idea and caption for this theme: {theme}"
        result = generate_text(prompt)
        st.write(result)
