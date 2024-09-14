# Cohere "fixing" notes, removing duplicates and fixing grammar 
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from screenRecorder import ScreenRecorder
import cohere


class GenerateTopics:
    def __init__(self):
        load_dotenv("C:/Users/prana/Documents/GitHub/sessions.ai/backend/.env")
        self.cohere_api = os.getenv("COHERE_API_KEY")

    def coherentTopics(self, notes, number):
        co = cohere.Client(api_key=self.cohere_api)
        response = co.chat(
            model="command-r-plus",
            message=notes + "Generate a list of " + str(number) + " topics from this string of notes. Numbered 1 to 5, no need for other text like an introduction or conclusion such 'Here is a list of 5 topics generated from the provided string of notes: '. Just the topics, numbered 1 to 5. ENSURE PROPER GRAMMAR, SYNTAX, AND SPELLING."
        )

        return response.text




    