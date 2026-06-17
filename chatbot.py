import json
import random
import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer data (only first time)
nltk.download('punkt')
nltk.download('punkt_tab')

# Load intents
with open('intents.json', 'r', encoding='utf-8') as file:
    intents = json.load(file)

def get_response(user_message):
    user_message = user_message.lower()
    user_words = word_tokenize(user_message)

    best_response = None
    highest_score = 0

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            pattern_words = word_tokenize(pattern.lower())

            # Calculate matching words
            score = len(set(user_words) & set(pattern_words))

            if score > highest_score:
                highest_score = score
                best_response = random.choice(intent['responses'])

    if highest_score > 0:
        return best_response

    return "I'm sorry, I couldn't understand your question. Could you please rephrase it?"

# Test locally
if __name__ == "__main__":
    print("Customer Service Chatbot")
    print("Type 'quit' to exit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("Bot: Goodbye!")
            break

        print("Bot:", get_response(user_input))