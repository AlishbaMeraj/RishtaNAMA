import streamlit as st
from openrouter_api import generate_text

def show_pickup_lines():
    st.header("🎯 Cute Pickup Lines Banaiye")

    mood = st.selectbox("Apka mood kya hai?", ["Shayari Style", "Funny", "Nerdy", "Filmy"])
    gender = st.radio("Select your intention:", ["Impress me", "I want to impress someone"])

    # ✨ Mood-specific instructions
    if mood == "Shayari Style":
        style_instruction = "Use poetic Urdu style with romantic flair — like modern shayari."
    elif mood == "Funny":
        style_instruction = "Be witty, humorous, and use playful desi rishta references."
    elif mood == "Nerdy":
        style_instruction = "Use smart, clever, techy or bookish lines with a romantic twist."
    elif mood == "Filmy":
        style_instruction = "Use Bollywood-style drama and flair — cheesy but charming."

    if st.button("Line Generate Karo 💘"):
        prompt = f"""
        Generate a {mood.lower()} Urdu-English pickup line for rishta context.
        Gender context: {"for a girl" if gender == "Impress me" else "for a boy"}.
        {style_instruction}
        The line should be 1–2 lines only, classy and cute.
        """

        try:
            with st.spinner("Generating line... 💌"):
                response = generate_text(prompt)
                pickup_line = response.strip()

            st.success("Mission rishta initiated — line tayyar hai 💡😉")
            st.markdown(f"🌟 **{pickup_line}**")
            st.text_area("📋 Ready to send — copy your perfect line below:", value=pickup_line, height=100)

            if st.button("🔁 Nai Line Try Karo"):
                st.rerun()

        except Exception as e:
            st.error("Kuch error aa gaya. Please try again later.")
