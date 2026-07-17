import streamlit as st

from agents.mood_agent import analyze_mood
from agents.journal_agent import analyze_journal
from agents.sleep_agent import analyze_sleep
from agents.mood_tracker import save_mood
from agents.mood_history import generate_mood_graph
from agents.meditation_agent import suggest_meditation
from agents.pdf_agent import create_wellness_pdf


st.set_page_config(
    page_title="MindCare AI",
    page_icon="🧠"
)

st.title("🧠 MindCare AI")
st.write("Your AI Mental Health Assistant")


# Store results
if "mood_result" not in st.session_state:
    st.session_state.mood_result = ""

if "journal_result" not in st.session_state:
    st.session_state.journal_result = ""

if "sleep_result" not in st.session_state:
    st.session_state.sleep_result = ""

if "meditation_result" not in st.session_state:
    st.session_state.meditation_result = ""


option = st.selectbox(
    "Choose a feature",
    [
        "Mood Analysis",
        "Journal Reflection",
        "Sleep Analysis",
        "Mood History",
        "Meditation Guide",
        "Generate Wellness Report"
    ]
)



if option in [
    "Mood Analysis",
    "Journal Reflection"
]:

    user_input = st.text_area(
        "Write your thoughts here:"
    )



elif option == "Sleep Analysis":

    hours = st.number_input(
        "Hours slept",
        min_value=0.0,
        max_value=24.0,
        value=8.0
    )

    quality = st.slider(
        "Sleep quality (1-10)",
        1,
        10,
        7
    )

    bedtime = st.time_input(
        "Bedtime"
    )

    wake_time = st.time_input(
        "Wake-up time"
    )

    feeling = st.text_area(
        "How did you feel after waking up?"
    )



if option == "Mood History":

    st.subheader("📈 Your Mood History")

    graph = generate_mood_graph()

    if graph:
        st.pyplot(graph)

    else:
        st.info(
            "No mood data available yet."
        )



if option == "Meditation Guide":

    mood = st.text_input(
        "Enter your mood"
    )

    intensity = st.selectbox(
        "Select intensity",
        [
            "Low",
            "Medium",
            "High"
        ]
    )


    if st.button("Get Meditation"):

        st.session_state.meditation_result = suggest_meditation(
            mood,
            intensity
        )

        st.subheader(
            "🧘 Meditation Suggestion"
        )

        st.write(
            st.session_state.meditation_result
        )



if option == "Generate Wellness Report":

    st.subheader(
        "📄 Create Wellness Report"
    )


    if st.button("Generate PDF"):

        pdf_file = create_wellness_pdf(
            st.session_state.mood_result,
            st.session_state.journal_result,
            st.session_state.sleep_result,
            st.session_state.meditation_result
        )


        with open(pdf_file, "rb") as file:

            st.download_button(
                label="Download Wellness Report PDF",
                data=file,
                file_name=pdf_file,
                mime="application/pdf"
            )



if st.button("Submit"):

    with st.spinner("Analyzing..."):


        if option == "Mood Analysis":

            if not user_input:
                st.warning(
                    "Please write something first."
                )
                st.stop()


            st.session_state.mood_result = analyze_mood(
                user_input
            )


            save_mood(
                st.session_state.mood_result["emotion"],
                st.session_state.mood_result["intensity"]
            )


            st.subheader(
                "📝 AI Analysis"
            )

            st.write(
                st.session_state.mood_result
            )


        elif option == "Journal Reflection":

            if not user_input:
                st.warning(
                    "Please write something first."
                )
                st.stop()


            st.session_state.journal_result = analyze_journal(
                user_input
            )


            st.subheader(
                "📝 AI Analysis"
            )

            st.write(
                st.session_state.journal_result
            )


        elif option == "Sleep Analysis":


            st.session_state.sleep_result = analyze_sleep(
                hours=hours,
                quality=quality,
                bedtime=str(bedtime),
                wake_time=str(wake_time),
                feeling=feeling
            )


            st.subheader(
                "📝 AI Analysis"
            )

            st.write(
                st.session_state.sleep_result
            )
