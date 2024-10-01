import pyttsx3

class VoiceOutput:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        print(f"Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

