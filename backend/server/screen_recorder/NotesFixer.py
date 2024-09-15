# Cohere "fixing" notes, removing duplicates and fixing grammar
import os
from dotenv import load_dotenv
from random import randint
from .ScreenRecorder import ScreenRecorder
import cohere
import json
import requests
from os import path
import sys
from .overlay import engage_overlay
from multiprocessing import Process

load_dotenv()


class NotesFixer:
    def __init__(self):
        self.recorder = ScreenRecorder()
        self.cohere_api = os.getenv("COHERE_API_KEY")

    def get_notes(self):
        recorded_study = self.recorder.run()  # Capture the study session
        co = cohere.Client(api_key=self.cohere_api)
        response = co.chat(
            model="command-r-plus",
            message=recorded_study
            + "\n\nEnsure the above is readable. No gibberish; if strings of characters are unredeemable, scratch them off. Get rid of the duplicates in this text and fix some of the grammar here. STAY ON TOPIC. Do not divert to a separate subject that you sense. This will be about studying a subject. EXTREMELY IMPORTANT: Only respond with the edited text. Do not bother expounding upon 'this is the edited text.' That is unnecessary.",
        )

        return (
            response.text
        )  # Return the final data if needed for debugging or further processing


def main():
    fixNotes = NotesFixer()

    while True:
        notes = fixNotes.get_notes()
        r = requests.post(
            "http://localhost:3001/package",
            data=notes,
            headers={"Content-Type": "text/plain", "session_filename": "ripbozo"},
        )
        print(r.text)
