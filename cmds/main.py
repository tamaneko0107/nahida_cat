import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{self.bot.latency*1000:.0f} ms')

def setup(bot):
    return bot.add_cog(Main(bot))
