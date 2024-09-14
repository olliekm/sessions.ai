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

    def fixNotes(self):
        recordedStudy = self.recorder.run() # set this to run loops later
        
co = cohere.Client(api_key="<YOUR API KEY>")

response = co.chat(
  model="command-r-plus",
  message="Write a title for a blog post about API design. Only output the title text."
)

print(response.text) # "The Art of API Design: Crafting Elegant and Powerful Interfaces"




    