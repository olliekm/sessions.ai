# Cohere "fixing" notes, removing duplicates and fixing grammar 
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from screenRecorder import ScreenRecorder
from parseNotes import NotesFixer
import cohere


class GenerateQuestions:
    def __init__(self):
        load_dotenv("C:/Users/prana/Documents/GitHub/sessions.ai/backend/.env")
        self.cohere_api = os.getenv("COHERE_API_KEY")

    def coherentQuestions(self, notes):
        co = cohere.Client(api_key=self.cohere_api)
        response = co.chat(
            model="command-r-plus",
            message=notes + "Generate a list of 5 questions about the notes posted above, no other reply."
        )

        return response.text

if "__main__" == __name__:
    generateQuestions = GenerateQuestions()
    generateQuestions.coherentQuestions()




    