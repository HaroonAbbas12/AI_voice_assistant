import speech_recognition as sr
from statics import BOT_NAME

class VoiceInput:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self, timeout=10):
        with self.microphone as source:
            print("Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            try:
                audio = self.recognizer.listen(source, timeout=timeout)
                print("Processing speech recognition...")
                user_input = self.recognizer.recognize_google(audio)
                print(f"prompt: {user_input}")  # Display the recognized input
                return user_input
            except sr.WaitTimeoutError:
                print("Listening timed out; no speech detected.")
                return None
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio.")
                return None
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return None

    def wait_for_wake_word(self, wake_word=f"{BOT_NAME}"):
        while True:
            print(f"Waiting for wake word: '{wake_word}'")
            user_input = self.listen(timeout=10)  # Listen for speech input
            if user_input:
                print(f"Recognized input: {user_input}")  # Display recognized input even before checking the wake word
                if wake_word.lower() in user_input.lower():
                    print(f"Wake word '{wake_word}' detected.")
                    return True
            print("Wake word not detected or no input. Continuing to listen...")
