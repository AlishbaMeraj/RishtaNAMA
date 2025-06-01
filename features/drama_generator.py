# features/drama_generator.py

import streamlit as st
from openrouter_api import generate_text

def show_drama_generator():
    st.subheader("🎬 Shaadi Drama Generator")
    scene = st.selectbox("Choose Scene Type:", ["Mehndi", "Nikkah", "Baraat", "Walima"])
    tone = st.selectbox("Choose Tone:", ["Comedy", "Emotional", "Overdramatic"])

    if st.button("Generate Scene"):
        prompt = f"""
        Write a short, funny and dramatic scene for a Pakistani shaadi event:
        Scene: {scene}
        Tone: {tone}
        Format: Short script style, with character dialogues, suitable for TikTok reel.
        Include names and emotional reactions.
        """
        try:
            with st.spinner("Generating Shaadi Drama... 🎭"):
                result = generate_text(prompt, max_tokens=300)
            st.success("Here's your drama scene:")
            st.write(result)
        except Exception:
            st.error("Oops! Something went wrong. Please try again later.")    
