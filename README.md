🎧 Mood Journal with Music & Mindfulness
A Streamlit-based web app that helps users check in with their emotions, receive mood-aligned music suggestions, and generate calming affirmations — all while tracking their mood history over time.

📌 What It Does
✅ Lets users select their current mood (e.g., Happy, Sad, Stressed).

🎶 Recommends music based on the selected mood using a curated list.

🤖 Generates a personalized affirmation using a local GPT-2 AI model.

📝 Logs each mood entry to a local file (mood_logs.json) with a timestamp.

📊 Displays an interactive mood history chart, filterable by time.

🌈 Features a modern, soothing UI with animated elements and styling.

🚀 How to Run It
1. Clone the repository or download the project
bash
Copy
Edit
git clone https://github.com/your-username/mood-journal-app.git
cd mood-journal-app
2. Install dependencies
Make sure you’re using Python 3.8 or later. Then run:

bash
Copy
Edit
pip install -r requirements.txt
Or manually:

bash
Copy
Edit
pip install streamlit transformers pandas altair
3. Run the app
bash
Copy
Edit
streamlit run app.py
The app will open in your browser at http://localhost:8501.

🧰 Tools & Libraries Used
Tool / Library	Purpose
Streamlit	UI framework for the web app
Transformers (Hugging Face)	Local GPT-2 model for affirmation generation
Altair	Mood frequency visualization
Pandas	Mood log processing
JSON / datetime	Data logging and timestamps
Custom CSS	Aesthetic and UX enhancements

📈 Features Highlight
Feature	Description
🎵 Mood-based Music	Hand-picked songs tied to user moods
🧘 AI Affirmations	GPT-2 generates affirmations like a mini mood coach
📊 Mood Chart	Visual log of emotion frequency
💾 Local Logging	JSON file stores mood history securely
💡 Beautiful UI	Calming gradients, animated bubbles, custom buttons

⚠️ Challenges Faced
Spotify API Limitations: Initially used Spotify for audio feature extraction, but issues with token access and rate limits led to shifting the project scope.

OpenAI Quota Errors: Switched to Hugging Face or local GPT-2 due to quota exhaustion.

Session State in Streamlit: Managing multiple user actions like recommendation vs. saving required careful use of st.session_state.

🚀 What I’d Improve with More Time
🧠 Add emotion intensity sliders or journal text input

🔊 Integrate real-time song previews using YouTube or Spotify embeds

📤 Add export or download mood history as CSV

☁️ Deploy via Streamlit Cloud or Docker for online use

🗃️ Use SQLite or Firebase for persistent user-specific data

🎯 Add clustering or emotion AI for smarter recommendations