import discord
from discord.ext import commands
from core.classes import Cog_Extension
import blue_archive.message as message

class React(Cog_Extension):
    @commands.command()
    async def test(self, ctx):
        embed = await message.Embed()
        await ctx.send(embed=embed)

def setup(bot):
    return bot.add_cog(React(bot))