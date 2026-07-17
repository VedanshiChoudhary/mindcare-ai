import csv
import os
from datetime import datetime


FILE_PATH = "data/moods.csv"


def save_mood(emotion, intensity):

    os.makedirs("data", exist_ok=True)

    file_exists = os.path.isfile(FILE_PATH)

    with open(FILE_PATH, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(
                ["Date", "Time", "Emotion", "Intensity"]
            )

        writer.writerow(
            [
                datetime.now().date(),
                datetime.now().strftime("%H:%M"),
                emotion,
                intensity
            ]
        )


def get_mood_history():

    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as file:

        reader = csv.DictReader(file)

        return list(reader)