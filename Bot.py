# This file will be mainly used for basic functionality of the bot.
import discord
from dotenv import load_dotenv
import os
import Responses

load_dotenv()

# This is the return function for sending the user messages
async def message(message, rmessage):
    try:
        response = Responses.test_response(message)
        await message.channel.send(rmessage)

    except Exception as test:
        print("Error has occured")

def bot():
    token = os.getenv("KEY")
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_run(): # Initial test that bot is online
        print(f'{client.user} is online!')

    client.run(token)