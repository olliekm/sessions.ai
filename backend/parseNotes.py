# Cohere "fixing" notes, removing duplicates and fixing grammar 
import os
from dotenv import load_dotenv, find_dotenv
from random import randint
from screenRecorder import ScreenRecorder
import cohere
import json
from os import path

class NotesFixer:
    def __init__(self):
        self.recorder = ScreenRecorder()
        load_dotenv("C:/Users/prana/Documents/GitHub/sessions.ai/backend/.env")
        self.cohere_api = os.getenv("COHERE_API_KEY")

    def coherentNotes(self):
        # File path for the JSON file
        json_file = 'sessionBatch1.json'
        
        # Initialize or load the JSON file
        if not path.exists(json_file):
            with open(json_file, 'w') as f:
                json.dump({"sessionNotes": []}, f)  # Create an empty JSON structure for sessionNotes
        
        # Open the file in read mode to load existing notes
        with open(json_file, 'r') as f:
            data = json.load(f)

        # Check if sessionNotes is a string (and empty), convert it to a list if so
        if isinstance(data.get('sessionNotes'), str):
            data['sessionNotes'] = []

        # Generate random stop value
        randomStop = randint(10, 15)
        
        for i in range(randomStop):
            recordedStudy = self.recorder.run()  # Capture the study session
            co = cohere.Client(api_key=self.cohere_api)
            response = co.chat(
                model="command-r-plus",
                message=recordedStudy + "\n\nEnsure the above is extremely readable. No gibberish, however if strings of characters are unredeemable, scratch them off. Get rid of the duplicates in this text and fix some of the grammar here. STAY ON TOPIC. Do not divert to a separate subject that you sense. This will be about studying a subject. EXTREMELY IMPORTANT: Only respond with the edited text. Do not bother expounding upon 'this is the edited text.' That is unnecessary."
            )
            
            # Add the response text to the sessionNotes list
            data['sessionNotes'].append({
                'iteration': i + 1,
                'fixed_notes': response.text
            })
            
            # Write the updated notes to the JSON file
            with open(json_file, 'w') as f:
                json.dump(data, f, indent=4)

        return data  # Return the final data if needed for debugging or further processing

if __name__ == '__main__':
    fixNotes = NotesFixer()
    fixNotes.coherentNotes()
