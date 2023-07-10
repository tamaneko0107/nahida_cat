import discord
from discord.ext import commands
from core.classes import Cog_Extension

class React(Cog_Extension):
    
    @commands.command()
    async def clear(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)

async def setup(bot):
    await bot.add_cog(React(bot))