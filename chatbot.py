import json
import random

with open("intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def get_response(message):

    message = message.lower()

    best_match = None
    highest_score = 0

    user_words = set(message.split())

    for intent in data["intents"]:

        for pattern in intent["patterns"]:

            pattern_words = set(pattern.lower().split())

            score = len(
                user_words.intersection(pattern_words)
            )

            if score > highest_score:

                highest_score = score

                best_match = random.choice(
                    intent["responses"]
                )

    if best_match:
        return best_match

    return (
        "I couldn't understand that request. Please ask about orders, refunds, shipping, payments, accounts or support."
    )