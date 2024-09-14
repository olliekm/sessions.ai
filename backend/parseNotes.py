# Cohere "fixing" notes, removing duplicates and fixing grammar 
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from screenRecorder import ScreenRecorder
import cohere


class NotesFixer:
    def __init__(self):
        self.recorder = ScreenRecorder()
        load_dotenv("C:/Users/prana/Documents/GitHub/sessions.ai/backend/.env")
        self.cohere_api = os.getenv("COHERE_API_KEY")

    def coherentNotes(self):
        recordedStudy = self.recorder.run() # set this to run loops later
        co = cohere.Client(api_key=self.cohere_api)
        response = co.chat(
            model="command-r-plus",
            message=recordedStudy + "\n\nEnsure the above is extremely readable. No gibberish, however if strings of characters are unredeemable, scratch them off. Get rid of the duplicates in this text and fix some of the grammar here. STAY ON TOPIC. Do not divert to a separate subject that you sense. This will be about studying a subject. EXTREMELY IMPORTANT: Only respond with the edited text. Do not bother expounding upon 'this is the edited text.' That is unnecessary."
        )

        return response.text

if "__main__" == __name__:
    fixNotes = NotesFixer()
    fixNotes.coherentNotes()




    