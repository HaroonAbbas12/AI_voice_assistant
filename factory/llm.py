import openai
from ..statics import OPENAI_API_KEY, MODEL_NAME, MAX_LIMIT_INPUT, LLM_TEMPERATURE

# Get the API key from the environment variable
openai.api_key = OPENAI_API_KEY
class GPTProcessor:
    def count_words(self, text):
        return len(text.split())

    def process(self, text):
        print(f"Processing with {MODEL_NAME}...")

        try:
            # Count words in the input text
            input_words = self.count_words(text)
            if input_words > MAX_LIMIT_INPUT:
                # Truncate to the first MAX_LIMIT_INPUT words
                text = ' '.join(text.split()[:MAX_LIMIT_INPUT]) + '...'
                print(f"Truncated input to {MAX_LIMIT_INPUT} words: {text}")

            response = openai.ChatCompletion.create(
                model=MODEL_NAME,
                temperature=LLM_TEMPERATURE,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant but are to the point. Be concise and limit the responses."},
                    {"role": "user", "content": text}
                ]
            )

            message_content = response.choices[0].message['content'].strip()
            total_tokens = response['usage']['total_tokens']  # Get total tokens used in the request
            print(f"{MODEL_NAME} response: {message_content}")
            print(f"Total tokens used: {total_tokens}")

            return message_content, total_tokens  # Return the message content and token usage
        except Exception as e:
            print(f"Error processing the text: {e}")
            return None, 0  # Return 0 tokens in case of error
