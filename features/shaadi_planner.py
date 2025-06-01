# features/shaadi_planner.py

import streamlit as st

def show_shaadi_planner():
    st.subheader("🗓️ Shaadi Planner (Coming Soon)")
    st.info("Plan your wedding tasks & countdown! 🚧 In progress...")
    st.markdown("### Shaadi Checklist")
tasks = ["Venue booked", "Dress ready", "Invitation sent"]
for task in tasks:
    st.checkbox(task)

