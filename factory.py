import speech_recognition as sr
import pyttsx3
import openai
import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')


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
                return self.recognizer.recognize_google(audio)
            except sr.WaitTimeoutError:
                print("Listening timed out; no speech detected.")
                return None
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio")
                return None
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return None

    def wait_for_wake_word(self, wake_word="Hey Bob"):
        while True:
            print(f"Waiting for wake word: '{wake_word}'")
            user_input = self.listen(timeout=10)  # Listen indefinitely
            if user_input:
                if wake_word.lower() in user_input.lower():
                    print(f"Wake word '{wake_word}' detected.")
                    return True
            print("Wake word not detected or no input. Continuing to listen...")


class GPTProcessor:
    def count_words(self, text):
        return len(text.split())

    def process(self, text):
        print("Processing with GPT-4o-mini...")

        try:
            # Count words in the input text
            input_words = self.count_words(text)
            if input_words > 100:
                # Truncate to the first 100 words
                text = ' '.join(text.split()[:100]) + '...'
                print(f"Truncated input to 50 words: {text}")

            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                temperature=0,
                messages=[
                    {"role": "system", "content": "Be concise and limit the response."},
                    {"role": "user", "content": text}
                ]
            )

            message_content = response.choices[0].message['content'].strip()
            total_tokens = response['usage']['total_tokens']  # Get total tokens used in the request
            print(f"GPT-4o-mini response: {message_content}")
            print(f"Total tokens used: {total_tokens}")

            return message_content, total_tokens  # Return the message content and token usage
        except Exception as e:
            print(f"Error processing the text: {e}")
            return None, 0  # Return 0 tokens in case of error

class VoiceOutput:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        print(f"Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

