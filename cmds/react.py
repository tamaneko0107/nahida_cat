import discord
from discord.ext import commands
from core.classes import Cog_Extension
import blue_archive.message as message

class React(Cog_Extension):
    @commands.hybrid_command(name="test",with_app_command=True, description="ブルアカニュース")
    async def test(self, ctx):
        await ctx.defer()
        embed = await message.Embed()
        await ctx.send(embed=embed)

    @commands.command()
    async def clear(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)

async def setup(bot):
    await bot.add_cog(React(bot))