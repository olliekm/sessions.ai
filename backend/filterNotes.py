# Cohere "fixing" notes, removing duplicates and fixing grammar 
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from screenRecorder import ScreenRecorder
import cohere


class NotesFilter:
    def __init__(self):
        self.recorder = ScreenRecorder()
        load_dotenv("C:/Users/prana/Documents/GitHub/sessions.ai/backend/.env")
        self.cohere_api = os.getenv("COHERE_API_KEY")

    def coherentFilter(self, notes, topics):
        co = cohere.Client(api_key=self.cohere_api)
        response = co.chat(
            model="command-r-plus",
            message="Notes: " + notes + "\nTopics: " + topics + "\n\nEnsure the above is extremely readable. No gibberish, however if strings of characters are unredeemable, scratch them off. STAY ON TOPIC. Do not divert to a separate subject that you sense. This will be about studying a subject. EXTREMELY IMPORTANT: Only respond with the edited text. Do not bother expounding upon 'this is the edited text.' That is unnecessary. Next, whatever you see in the notes, keep the notes that have to do with the TOPICS involved. Filter out everything else."
        )

        return response.text

if "__main__" == __name__:
    fixNotes = NotesFilter()
    fixNotes.coherentFilter()




    