#This is the bot.py file
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('')

client = discord.client()

@client.event
async def on_ready()
    print(f'{client.user} successfully connected to discord!')

client.run(TOKEN)