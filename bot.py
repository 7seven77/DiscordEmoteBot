# bot.py
from directory import Directory
import os
from os import name
import random
import re

import discord

# Imported for easy type hinting
from discord.ext.commands import Context
# Used in bot creation
from discord.ext import commands

from dotenv import load_dotenv

from emote import emoteCog
from db import db

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

    commands : list[str] = Directory.getImageDirectories()
    for command in commands:
        bot.add_cog(emoteCog(command))

    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="you for commands .help"))

    # print('Database init', end ='\r')
    # db.setUp()

    print('  - Bot ready -  ')

##### Bot commands

@bot.command(name='help')
async def help(ctx : Context, group : str = None) -> None:
    if group == None:
        await showGroups(ctx)
    else:
        await showEmotes(ctx, group)

async def showGroups(ctx: Context) -> None:
    groups : list[str] = Directory.getImageDirectories()

    message = discord.Embed(title =f'Commands', description=f'Commands you can use to show an emote',color=0x800080)

    size : int = len(groups)
    inline : bool = True
    for count in range(size):
        group : str = groups[count]
        numberOfEmotes : int = len(Directory.getImageNames(group))
        message.add_field(name=group, value=f"Emotes: {numberOfEmotes}", inline=inline)

    message.add_field(name='Commands are invoked using `.{Command} {Name}`',
        value='Eg. `.xqc L`', inline=False)
    await ctx.send(embed=message)

async def showEmotes(ctx: Context, group: str):
    files : list[str] = Directory.getImageNames(group)
    if files == None:
        await ctx.send("This is an invalid command")
        return
    emotes = [fileName[:-4] for fileName in files]
    await ctx.send(emotes)

@bot.command(name='u')
async def upload(ctx: Context, slot: int):
    attachments = ctx.message.attachments
    if attachments == []:
        await ctx.send("Upload an image")
        return
    url: str = attachments[0].url

    maxSlots: int = 3
    if slot < 1 or slot > maxSlots:
        await ctx.send(f'Please enter a whole number greater than 0 and less than {maxSlots + 1}')
        return
    db.setEmote(str(ctx.author.id), str(slot), url)
    await ctx.send("Your emote has been saved")

@bot.command(name='c')
async def custom(ctx: Context, slot: int):
    url: str = db.getEmote(str(ctx.author.id), str(slot))

    if url == None:
        await ctx.send("Invalid number")
        return
    
    await ctx.send(url)

# Start the bot
print("Starting bot", end='\r')
bot.run(TOKEN) 