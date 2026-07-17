import pandas as pd
import matplotlib.pyplot as plt
import os


FILE_PATH = "data/moods.csv"


def generate_mood_graph():

    if not os.path.exists(FILE_PATH):
        return None

    df = pd.read_csv(FILE_PATH)

    mood_scores = {
        "Happy": 5,
        "Calm": 4,
        "Neutral": 3,
        "Stress": 2,
        "Sad": 1,
        "Anxious": 2
    }

    df["Score"] = df["Emotion"].map(mood_scores)

    df["Date"] = pd.to_datetime(df["Date"])

    fig, ax = plt.subplots()

    ax.plot(
        df["Date"],
        df["Score"],
        marker="o"
    )

    ax.set_title("Mood History")
    ax.set_xlabel("Date")
    ax.set_ylabel("Mood Score (1-5)")

    ax.set_ylim(0, 5)

    return fig