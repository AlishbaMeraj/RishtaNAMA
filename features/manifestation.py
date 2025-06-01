# features/manifestation.py

import streamlit as st
from openrouter_api import generate_text

def show_manifestation():
    st.subheader("🌸 Manifest Your Dream Rishta")
    user_input = st.text_area("Enter your dream rishta description (Urdu or English):", "")

    if st.button("Generate Manifestation"):
        if user_input.strip() == "":
            st.warning("Please describe your dream rishta to manifest.")
            return

        prompt = f"""
Aap ek romantic Urdu shayar hain. Aapko ek pyari dua aur shayari likhni hai jo kisi ke dream rishta ke liye ho.  
Shayari mein mohabbat, umeed aur faith ka izhaar ho.  
Rishta ki qualities: {user_input}  
Urdu aur thodi English mix karein, poetic aur dil se likhein.
"""
        try:
            with st.spinner("Manifesting your rishta... 💖"):
                result = generate_text(prompt)
            st.success("Here's your manifestation:")
            st.write(result)

        except Exception as e:
            st.error("Oops! Something went wrong. Please try again later.")
        

