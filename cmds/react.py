import discord
from discord.ext import commands
from core.classes import Cog_Extension
import blue_archive.message as message
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=3)

class React(Cog_Extension):
    @commands.hybrid_command(name="test",with_app_command=True, description="ブルアカニュース")
    async def test(self, ctx):
        await ctx.defer()
        future = executor.submit(message.Embed)
        future.add_done_callback(lambda x: self.bot.loop.create_task(self.send_embed(ctx, x.result())))

    async def send_embed(self, ctx, embed):
        await ctx.send(embed=embed)

        
    @commands.command()
    async def clear(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)

async def setup(bot):
    await bot.add_cog(React(bot))