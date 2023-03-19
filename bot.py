# This file will be mainly used for basic functionality of the bot.
import discord
from dotenv import load_dotenv
import os
import responses

load_dotenv()


# This is the function for sending the user messages
async def send_message(message, user_message, private):
    try:
        response = responses.test_response(user_message)
        await message.author.send(response) if private else await message.channel.send(response)

    except Exception as test:
        print(test)


# Main function that runs the bot
def run_Mindfulbot():
    # Sets the key and default intents per Discord
    token = os.getenv("KEY")
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # Confirms bot is online
    @client.event
    async def on_ready():
        print(f'{client.user} is online!')

    # Takes the user message when sent then runs the send_message function
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        # Parses message attributes into needed attributes
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Prints contents of the message
        print(f'{username} said: "{user_message}" ({channel})')

        # Parses if message is to be private or not then sends message
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, private=True)
        else:
            await send_message(message, user_message, private=False)

    # Run the bot!
    client.run(token)
