import openai
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()
# Get the API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')


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
