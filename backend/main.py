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
# Fix notes
# Generate topics
    
    def generateTopics(self, numberOfTopics):
        print(self.topicsGeneration.coherentTopics(self.fixNotes.coherentNotes(), numberOfTopics)) # Topics

# "Keep notes" to do with undiscarded notes

    def retainNotes(self, topics):
        pattern = r'\d+\.\s*"[^"]+":[^0-9]*?(?=\d+\.\s*"[^"]+":|$)'

        # Find all matches
        matches = re.findall(pattern, input_string, re.DOTALL)

        # Clean up the matches and store them in a list
        topics = [match.strip() for match in matches if match.strip()]

        # Print the result
        for i, topic in enumerate(topics, start=1):
            print(f"{i}. {topic}")

        removeNumber = input("\n\n")

        topics = topics.remove(int(removeNumber) - 1)
        return topics

if "__main__" == __name__:
    run = Main()
    run.retainNotes(retainNotes(5))
