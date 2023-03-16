# This file is going to be used to hold all the files that the bot will use when responding to the user.

def responses(message: str) -> str:
    if message == "test":
        return "Hello there!"
