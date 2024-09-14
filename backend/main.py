from screenRecorder import ScreenRecorder
from parseNotes import NotesFixer
from generateTopics import GenerateTopics
from generateQuestions import GenerateQuestions

class Main:
    def __init__(self):
        self.screenRecorder = ScreenRecorder()
        self.fixNotes = NotesFixer()
        self.topicsGeneration = GenerateTopics()
        self.questionsGeneration = GenerateQuestions()

# Record the screen (20s for testing)
    
    def generateTopics(self):
        print(self.topicsGeneration.coherentTopics(self.fixNotes.coherentNotes()))

if "__main__" == __name__:
    run = Main()
    run.generateTopics()
