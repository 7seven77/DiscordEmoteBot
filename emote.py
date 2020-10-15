from directory import Directory
import discord
import os

from discord.ext import commands
from image import getEmoteFromFiles

class emoteCog(commands.Cog):
    def __init__(self, prefix : str) -> None:
        self.prefix = prefix
        self._emote.name = prefix

    @commands.command(name='emote')
    async def _emote(self, ctx, name : str) -> None:
        # Delete the original method
        try:
            await ctx.message.delete()
        except:
            await ctx.send("Please give me the permissions I need")

        path : str = Directory.getImagePath(self.prefix, name)
        if path != None:
            await ctx.send(file=getEmoteFromFiles(path))
        else:
            await ctx.send("Not a valid emote")
