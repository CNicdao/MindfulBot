# This file is going to be used to hold all the files that the bot will use when responding to the user.
import discord

# Basic test responses
def test_response(message: str) -> str:
    user_input = message.lower()

    if user_input == 'hello':
        return "Hey!"

    if user_input == 'why':
        return "cause why not?"

    if user_input == 'send me a complement':
        return complements

    else:
        return "Sorry, didn't catch that!"

complements = "You look great today!"