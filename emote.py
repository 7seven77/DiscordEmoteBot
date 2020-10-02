import discord
import os

from discord.ext import commands

class emoteCog(commands.Cog):

    @commands.command(name='emote', aliases=['e'])
    async def emote(self, ctx, name : str):
        # Delete the original method
        await ctx.message.delete()

        path : str = f'./images/pokimane/{name}.png'
        if os.path.isfile(path):
            await ctx.send(file=discord.File(path))
        else:
            await ctx.send("Not a valid emote")
