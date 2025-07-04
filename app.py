import streamlit as st
from mood_songs import mood_to_songs
from utils.gpt_affirmation import get_affirmation
import json
from datetime import datetime
import os
import pandas as pd
import altair as alt
from transformers import pipeline

# Load once at module level
generator = pipeline("text-generation", model="gpt2")

# Set page config with custom styling
st.set_page_config(page_title="Mood Journal with Music", page_icon="🎧", layout="wide")
st.title("🎧 Mood Journal with Music & Mindfulness")

# Custom CSS for soothing and attractive design
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #a3d8f4, #90ee90);
        background-size: cover;
        background-attachment: fixed;
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    .wave-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url('https://www.transparenttextures.com/patterns/wave.png');
        opacity: 0.1;
        z-index: -1;
    }
    .stButton>button {
        background-color: #4a90e2;
        color: white;
        border-radius: 20px;
        padding: 10px 20px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #357abd;
        transform: scale(1.05);
    }
    .affirmation-box {
        background-color: #2e8b57;
        padding: 20px;
        border-radius: 15px;
        color: #ffffff;
        font-family: 'Georgia', serif;
        font-style: italic;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .welcome-text {
        font-size: 18px;
        color: #ffffff;
        background-color: #3cb371;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .mood-history {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
    }
    .bubble {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.2);
        animation: float 10s infinite;
    }
    @keyframes float {
        0% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add animated bubbles for background effect
for i in range(5):
    st.markdown(
        f'<div class="bubble" style="width: {20 + i * 20}px; height: {20 + i * 20}px; '
        f'left: {i * 20}%; top: {i * 20}%; animation-delay: {i * 2}s;"></div>',
        unsafe_allow_html=True
    )

# Welcome message with styled text
st.markdown('<div class="welcome-text">🌿 Welcome to your daily mood check-in. Select how you feel today and receive music suggestions and a calming affirmation to guide your day.</div>', unsafe_allow_html=True)

# Layout with columns
col1, col2 = st.columns([1, 2])

with col1:
    mood = st.selectbox("How are you feeling today? 🌟", list(mood_to_songs.keys()), key="mood_select")
    if st.button("Get Recommendations 🎶", key="recommend_btn"):
        st.session_state.recommendations = True
    if st.button("Save Mood 📅", key="save_btn"):
        st.session_state.save_mood = True

with col2:
    if "recommendations" in st.session_state and st.session_state.recommendations:
        st.subheader(f"🎵 Songs to match your mood: *{mood}*")
        for song in mood_to_songs[mood]:
            st.write(f"- {song}")

        st.divider()
        st.subheader("🧘‍♀️ Your Affirmation:")
        with st.spinner("Generating affirmation..."):
            affirmation = get_affirmation(mood)
        st.markdown(f'<div class="affirmation-box">{affirmation}</div>', unsafe_allow_html=True)
        if st.button("New Affirmation 🔄", key="new_affirmation"):
            st.session_state.recommendations = False  # Trigger regeneration

    if "save_mood" in st.session_state and st.session_state.save_mood:
        log_entry = {"mood": mood, "timestamp": datetime.now().isoformat()}
        log_file = "mood_logs.json"
        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                logs = json.load(f)
        else:
            logs = []
        logs.append(log_entry)
        with open(log_file, "w") as f:
            json.dump(logs, f, indent=2)
        st.success("Mood saved successfully! 📝", icon="✅")
        st.session_state.save_mood = False

# Mood History Chart
st.divider()
st.markdown('<div class="mood-history">', unsafe_allow_html=True)
st.subheader("📊 Mood History")

time_filter = st.radio("Time Filter:", ["All Time", "Last 7 Days"], horizontal=True, key="time_filter")
if os.path.exists("mood_logs.json"):
    with open("mood_logs.json", "r") as f:
        logs = json.load(f)

    df = pd.DataFrame(logs)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["day"] = df["timestamp"].dt.date

    if time_filter == "Last 7 Days":
        df = df[df["timestamp"] >= datetime.now() - pd.Timedelta(days=7)]

    mood_counts = df["mood"].value_counts().reset_index()
    mood_counts.columns = ["mood", "count"]

    chart = alt.Chart(mood_counts).mark_bar().encode(
        x=alt.X("mood:N", title="Mood", sort=list(mood_to_songs.keys())),
        y=alt.Y("count:Q", title="Frequency"),
        color=alt.Color("mood:N", scale=alt.Scale(scheme="category10"))
    ).properties(
        title=f"Mood Frequency ({time_filter})",
        width=600,
        height=300
    ).interactive()

    st.altair_chart(chart, use_container_width=True)
else:
    st.info("No mood history yet. Save a mood above to begin logging. 🌱")

st.markdown('</div>', unsafe_allow_html=True)