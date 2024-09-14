from screenRecorder import ScreenRecorder
from parseNotes import NotesFixer
from generateTopics import GenerateTopics
from generateQuestions import GenerateQuestions
from filterNotes import NotesFilter
import re

class Main:
    def __init__(self):
        self.screenRecorder = ScreenRecorder()
        self.fixNotes = NotesFixer()
        self.topicsGeneration = GenerateTopics()
        self.questionsGeneration = GenerateQuestions()
        self.filteredNotes =  NotesFilter()

# Record the screen (20s for testing)
# Fix notes
# Generate topics

    def generateNotes(self):
        self.fixNotes.coherentNotes()
    
    def generateTopics(self, numberOfTopics):
        print(self.topicsGeneration.coherentTopics(self.fixNotes.coherentNotes(), numberOfTopics)) # Topics
        return (self.topicsGeneration.coherentTopics(self.fixNotes.coherentNotes(), numberOfTopics))
    
    def filterNotes(self, notes, topics):
        print(self.filteredNotes.coherentFilter(notes, topics))

    def questionGeneration(self, notes):
        print(self.questionsGeneration.coherentQuestions(notes))
        

if "__main__" == __name__:
    run = Main()
    run.generateTopics(5)
