import discord
import os

from discord.ext import commands
from image import getEmote

class emoteCog(commands.Cog):
    def __init__(self, prefix : str) -> None:
        self.prefix = prefix
        self._emote.name = prefix

    @commands.command(name='emote')
    async def _emote(self, ctx, name : str) -> None:
        # Delete the original method
        await ctx.message.delete()

        path : str = f'./images/{self.prefix}/{self.prefix}{name}.png'
        if os.path.isfile(path):
            await ctx.send(file=getEmote(path))
        else:
            await ctx.send("Not a valid emote")
