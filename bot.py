# bot.py
import os
import random
import re

import discord
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

@bot.command(name='emote', aliases=['e'])
async def emote(ctx, name : str):
    # Delete the original method
    await ctx.message.delete()

    path : str = f'./images/pokimane/{name}.png'
    if os.path.isfile(path):
        await ctx.send(file=discord.File(path))
    else:
        await ctx.send("Not a valid emote")

# Start the bot
bot.run(TOKEN) 