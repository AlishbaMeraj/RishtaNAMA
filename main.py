# main.py

import streamlit as st
from dotenv import load_dotenv
import os
from features.pickup_line_generator import show_pickup_lines


# Load .env file for API key
load_dotenv()
API_KEY = os.getenv('OPENROUTER_API_KEY')

# Page Configuration
st.set_page_config(page_title="RishtaNAMA 💖", layout="wide", page_icon="💖")

st.title("RishtaNAMA 💖 — Your AI Rishta Assistant")

# Import feature functions
from features.manifestation import show_manifestation
from features.bio_beautifier import show_bio_beautifier
from features.drama_generator import show_drama_generator
from features.dp_frame import show_dp_frame
from features.rishta_quiz import show_rishta_quiz
from features.shaadi_planner import show_shaadi_planner

# Sidebar menu with user-friendly Urdu-English + emojis
menu = [
    "Apni Dua Likhiye 💌",
    "Bio Ko Khoobsurat Banaiye 💖",
    "Cute Pickup Lines Banaiye 🎯",
    "Shaadi Ka Mazedar Drama 🎭",
    "DP Frame Aur Caption Banaiye 📸",
    "Apna Rishta Quiz Kheliye 🧩",
    "Shaadi Planner Aur Checklist 📅",
    
]

choice = st.sidebar.selectbox("Apni Pasandida Feature Chuney", menu)

# Conditional rendering of features with matching choices
if choice == "Apni Dua Likhiye 💌":
    show_manifestation()

elif choice == "Bio Ko Khoobsurat Banaiye 💖":
    show_bio_beautifier()

elif choice == "Shaadi Ka Mazedar Drama 🎭":
    show_drama_generator()

elif choice == "DP Frame Aur Caption Banaiye 📸":
    show_dp_frame()

elif choice == "Apna Rishta Quiz Kheliye 🧩":
    show_rishta_quiz()

elif choice == "Shaadi Planner Aur Checklist 📅":
    show_shaadi_planner()

elif choice == "Cute Pickup Lines Banaiye 🎯":
    show_pickup_lines()    
st.markdown("---")
st.markdown("Made with 💖 by Alishba Meraj | [GitHub](https://github.com/AlishbaMeraj/RishtaNAMA.git) | [LinkedIN](https://www.linkedin.com/in/alishba-meraj-7034752ba?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
