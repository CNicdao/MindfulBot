# This file will be mainly used for basic functionality of the bot.
import discord
import os
import Responses


# This is the return function for sending the user messages
async def message(message, response):
    try:
        response = Responses.responses(message)
        await message.author.send(response)

    except Exception as test:
        print("Error has occured")

def bot():
    token = os.getenv("KEY")
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
