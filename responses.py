# This file is going to be used to hold all the files that the bot will use when responding to the user.

# Basic test responses
def test_response(message: str) -> str:
    user_input = message.lower()

    if user_input == 'hello':
        return "Hey you!"

    if user_input == 'why':
        return ":)"

    else:
        return "Sorry, didn't catch that!"
