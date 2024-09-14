# Cohere "fixing" notes, removing duplicates and fixing grammar 
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from screenRecorder import ScreenRecorder
import cohere


class GenerateTopics:
    def __init__(self):
        load_dotenv("C:/Users/prana/Documents/GitHub/sessions.ai/backend/.env")
        self.cohere_api = os.getenv("COHERE_API_KEY")

    def coherentTopics(self, notes):
        co = cohere.Client(api_key=self.cohere_api)
        response = co.chat(
            model="command-r-plus",
            message=notes + "Generate a list of 5 topics from this string of notes."
        )

        return response.text

if "__main__" == __name__:
    fixNotes = GenerateTopics()
    fixNotes.coherentTopics()




    