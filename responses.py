# This file is going to be used to hold all the files that the bot will use when responding to the user.
import discord
import random

# Basic test responses
def test_response(message: str) -> str:
    user_input = message.lower()

    if user_input == 'hello':
        return "Hey!"

    if user_input == 'why':
        return "cause why not?"

    # Sends the user complements!
    if user_input == 'send me a complement':
        option = random.randint(0,3)
        return complements[option]

    else:
        return "Sorry, didn't catch that!"

# A list of complements
complements = ["You look great today!","You're really nice!","I'm proud of you!",
               "You're super cute!"]