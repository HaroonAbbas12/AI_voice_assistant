from factory.input import VoiceInput
from factory.output import VoiceOutput
from factory.llm import GPTProcessor

class MainAssistant:
    def __init__(self):
        self.voice_input = VoiceInput()
        self.processor = GPTProcessor()
        self.voice_output = VoiceOutput()

    def run(self):
        print("Starting the assistant..")
        while True:
            # Wait for the wake word
            if self.voice_input.wait_for_wake_word():
                self.voice_output.speak("How can I help you?")
                user_input = self.voice_input.listen(timeout=5)

                if user_input:
                    response, tokens_used = self.processor.process(user_input)

                    if response:
                        self.voice_output.speak(response)
                        print(f"Total tokens used in this interaction: {tokens_used}")
                    else:
                        self.voice_output.speak("Sorry, I couldn't process that.")
                else:
                    self.voice_output.speak("Sorry, I didn't catch that.")

                print("Waiting for wake word again...")

if __name__ == "__main__":
    assistant = MainAssistant()
    assistant.run()
