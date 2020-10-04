# bot.py
import os
from os import name
import random
import re

import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord.ext.commands import context
from dotenv import load_dotenv

from emote import emoteCog

# Get the bot token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set the bot prefix
botPrefix = str(os.getenv('BOT_PREFIX'))
bot = commands.Bot(command_prefix=botPrefix)

bot.remove_command('help')

# A blank entry for an embedded message
blank : str = '\u200B'
##### Bot events

@bot.event
async def on_ready():
    print('Adding cogs', end ='\r')
    bot.add_cog(emoteCog("poki"))
    bot.add_cog(emoteCog("xqc"))

    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="you for commands .help"))

    print('  - Bot ready -  ')

##### Bot commands

@bot.command(name='help')
async def help(ctx : Context, group : str = None) -> None:
    if group == None:
        await showGroups(ctx)
    else:
        await showEmotes(ctx, group)

async def showGroups(ctx : Context) -> None:
    groups : list[str] = os.listdir(os.path.join('.', 'images'))

    message = discord.Embed(title =f'Commands', description=f'Commands you can use to show an emote',color=0x800080)

    size : int = len(groups)
    inline : bool = False
    for count in range(size):
        if count == size - 1:
            inline = True
        message.add_field(name=groups[count], value=blank, inline=inline)

    #message.add_field(name=blank, value=blank, inline=False)
    message.add_field(name='Commands are invoked using `.{Command} {Name}`',
        value='Eg. `.xqc L`', inline=False)
    await ctx.send(embed=message)

async def showEmotes(ctx : Context, group : str):
    path : str = os.path.join('.', 'images', group)
    if not os.path.isdir(path):
        await ctx.send("This is an invalid command")
        return
    fileNames : list = os.listdir(path)
    emotes = [fileName[:-4] for fileName in fileNames]
    await ctx.send(emotes)

# Start the bot
print("Starting bot", end='\r')
bot.run(TOKEN) 