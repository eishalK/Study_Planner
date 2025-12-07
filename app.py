import streamlit as st
import pandas as pd

from Myagents.planner import PlannerAgent
from Myagents.calender_agent import CalendarAgent
from Myagents.revision_agent import RevisionAgent
from Myagents.summary_agent import SummaryAgent

from cores.utils import parse_time_slots

# --------------------------------------------------------
# 🎨 THEME SETTINGS
# --------------------------------------------------------
st.set_page_config(
    page_title="AI Study Scheduler",
    page_icon="📚",
    layout="wide"
)

# Top-right theme toggle
col1, col2, col3 = st.columns([6, 6, 2])  # last small column for toggle
with col3:
    theme_mode = st.radio("", ["Light", "Dark"], index=0, horizontal=True)

# Apply CSS based on theme
if theme_mode == "Dark":
    st.markdown(
        """
        <style>
        body, .stApp {
            background-color: #0e1117 !important;
            color: #E0E0E0 !important;
        }
        .stTextInput, .stTextArea, .stSelectbox, .stSlider, .stRadio {
            background-color: #1a1d23 !important;
            color: #E0E0E0 !important;
        }
        h1, h2, h3 {
            color: white !important;   
        }
        p, span {
            color: #E0E0E0 !important;
        }
        strong {
            color: #FF69B4 !important;
        }
        th {
            color: #FFA500 !important;
        }
        div.stButton > button {
           background-color: #4CAF50 !important;
           color: black !important;
           border-radius: 8px;
           padding: 0.5em 1em;
           font-size: 16px;
           font-weight: bold;
           transition: background-color 0.3s;
        }
        div.stButton > button:hover {
            background-color: #45a049 !important;
            color: black !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #ffffff !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------------
# MAIN UI
# --------------------------------------------------------
st.markdown(
    """
    <h1 style='text-align:center; color:black;'>
        📚 AI Study Scheduler (Agent-Based)
    </h1>
    <p style='text-align:center; font-size:18px;'>
        Convert your short-term academic goals into a structured, realistic<br>
        day-by-day study schedule using intelligent AI agents.
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------------
# Step 1: Plan Duration (1 week or 2 weeks)
# --------------------------------------------------------
st.subheader("📅 Step 1: Choose Plan Duration")
duration = st.radio(
    "Do you want to make a 1-week or 2-week plan?", 
    [7, 14], 
    index=0,
    horizontal=True
)

# --------------------------------------------------------
# Step 2: Goal and Topics
# --------------------------------------------------------
st.subheader("🎯 Step 2: What are you preparing for?")
goal = st.text_input("Describe your exam / project / milestone:")

st.subheader("📘 Step 3: Enter Topics & Difficulty Level")
topics_raw = st.text_area("Enter topics (comma-separated):")

if topics_raw:
    topics = [t.strip() for t in topics_raw.split(",")]
    st.write("### Adjust topic difficulty (1 = Easy, 5 = Hard):")
    difficulty = {t: st.slider(f"{t} difficulty", 1, 5, 3) for t in topics}
else:
    topics = []
# --------------------------------------------------------
# Step 4: Daily Available Hours
# --------------------------------------------------------
st.subheader("⏳ Step 4: Daily Available Study Hours")

# Initialize session state for hours if not already done
if "hours_dict" not in st.session_state:
    st.session_state.hours_dict = {}

weeks = 2 if duration == 14 else 1
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop over weeks
for week in range(1, weeks + 1):
    st.markdown(f"### Week {week}")
    cols = st.columns(7)
    for idx, day in enumerate(days):
        key = f"week{week}_{day}"
        default_val = st.session_state.hours_dict.get(key, 2.0)
        st.session_state.hours_dict[key] = cols[idx].number_input(
            day,
            min_value=0.0,
            max_value=10.0,
            value=default_val,
            key=key
        )

# Filter only days with hours > 0 and convert to time slots
time_slots = {}
for week in range(1, weeks + 1):
    for day in days:
        key = f"week{week}_{day}"
        hours = st.session_state.hours_dict.get(key, 0)
        if hours > 0:
            time_slots[key] = [f"Hour {i+1}" for i in range(int(hours))]

available_days = list(time_slots.keys())  # pass this to CalendarAgent

# --------------------------------------------------------
# Step 5: Generate Button
# --------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
generate_btn = st.button("🚀 Generate My Study Plan", use_container_width=True)

if generate_btn:
    if not goal or not topics:
        st.error("Please enter a goal and at least one topic.")
    else:
        with st.spinner("⏳ Generating your optimized plan using AI agents..."):
            # Planner Agent
            planner = PlannerAgent(topics, difficulty)
            plan = planner.plan_topics()

            calendar = CalendarAgent(
                topic_order=plan["topic_order"],
                weights=plan["weights"],
                time_slots=time_slots,
                all_days=available_days
            )
            schedule_df = calendar.create_calendar()

            if schedule_df.empty:
                st.error("⚠️ Could not generate a schedule. Please check your topics and available time slots.")
            else:
            # Revision Agent
                revision_agent = RevisionAgent(schedule_df, difficulty)
                final_schedule = revision_agent.add_revision()

               

            # Summary Agent
                summary_agent = SummaryAgent(final_schedule, goal)
                summary = summary_agent.summarize()


            # Results Section
                st.success("🎉 Study Plan Generated Successfully!")
                st.markdown("### 📄 Summary")
                st.write(summary)
                st.markdown("### 🗓 Final Study Schedule")
                st.dataframe(final_schedule, use_container_width=True)

                st.download_button(
                "📥 Download as CSV",
                data=final_schedule.to_csv(index=False),
                file_name="study_schedule.csv",
                use_container_width=True
                )