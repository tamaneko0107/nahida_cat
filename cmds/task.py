import discord
from datetime import datetime, time, timedelta, timezone
from discord.ext import tasks, commands
from core.classes import Cog_Extension
import asyncio


utc_plus_8 = timezone(timedelta(hours=8))

times = [
    time(second=10, tzinfo=utc_plus_8)
]

class Task(Cog_Extension):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lock = asyncio.Lock()
        self.send_test.start()

    async def cog_unload(self):
        self.send_test.stop()

    @tasks.loop(seconds=1)
    async def send_test(self):
        async with self.lock:
            now = datetime.now(utc_plus_8)
            if now.second == 10:
                channel = self.bot.get_channel(993457414236020776)
                await channel.send("test")

    async def send_embed(self, ctx, embed):
        await ctx.send(embed=embed)
    

async def setup(bot):
    await bot.add_cog(Task(bot))