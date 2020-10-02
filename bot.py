# bot.py
import os
import random
import re

from discord.ext import commands
from dotenv import load_dotenv

# Get the bot token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set the bot prefix
botPrefix = str(os.getenv('BOT_PREFIX'))
bot = commands.Bot(command_prefix=botPrefix)

##### Bot events

@bot.event
async def on_ready():
    print('Bot ready')

##### Bot commands

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello')

# Start the bot
bot.run(TOKEN) 