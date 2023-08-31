import openai
import re
import time  # for sleep
import os
from dotenv import load_dotenv

# Define function to append the translated text to a file
def append_to_book(file_path, content):
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(content)

# Function to split text into smaller parts based on sentence boundaries
def split_text(text, max_length):
    sentences = re.split('([.!?]"?)\s+', text)
    stitched_sentences = ["".join(x) for x in zip(sentences[::2], sentences[1::2])]
    
    parts = []
    current_part = ''
    for sentence in stitched_sentences:
        if len(current_part) + len(sentence) < max_length:
            current_part += sentence
        else:
            parts.append(current_part)
            current_part = sentence

    if current_part:
        parts.append(current_part)

    return parts

# Function to translate text using GPT-3.5-turbo
def translate_text(text, input_language, output_language, model):
    messages = [
        {"role": "system", "content": f"You are a helpful assistant that translates {input_language} to {output_language}."},
        {"role": "user", "content": f"Translate the following {input_language} text to {output_language}: {text}"}
    ]
    
    try:
        response = openai.ChatCompletion.create(
          model=model,
          messages=messages
        )
        return response['choices'][0]['message']['content']
    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")
        print("Retrying in 5 seconds...")
        time.sleep(5)
        return translate_text(text, input_language, output_language, model)  # Retry

# Main function
def main():
    load_dotenv()
    # API KEY
    openai.api_key = os.getenv("MY_API_KEY")
    # Input and output file paths
    input_file_path = os.getenv("INPUT_FILE_PATH")
    output_file_path = os.getenv("OUTPUT_FILE_PATH")
    # Input and output languages
    input_language = os.getenv("INPUT_LANGUAGE")
    output_language = os.getenv("OUTPUT_LANGUAGE")

    # Model type
    model = "gpt-3.5-turbo"

    with open(input_file_path, 'r', encoding='utf-8') as f:
        english_text = f.read()

    # Maximum length for each API call (halved from the original value)
    max_length = 1160  # Aligned with max_tokens based on estimation
    
    # Split the text into smaller parts
    parts = split_text(english_text, max_length)
    
    print(f"Total parts to translate: {len(parts)}")
    
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write('')  # This clears the existing content

    # Translate each part and append to file
    for i, part in enumerate(parts):
        print(f"Translating part {i+1}...")
        translated_part = translate_text(part, input_language, output_language, model)
        append_to_book(output_file_path, translated_part)
        print(f"Finished translating part {i+1}")


# Main function
if __name__ == "__main__":
    main()