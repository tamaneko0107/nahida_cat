import discord
from datetime import datetime, time, timedelta, timezone
from discord.ext import tasks, commands
from core.classes import Cog_Extension
import asyncio
import os
import json
from cmds.main import merge_dict, value_exists
import blue_archive.message as message
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=3)


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

    @commands.hybrid_command(name="test",with_app_command=True, description="ブルアカニュース")
    async def test(self, ctx):
        await ctx.defer()
        future = executor.submit(message.Embed)
        future.add_done_callback(lambda x: self.bot.loop.create_task(self.send_embed(ctx, *x.result())))

    async def send_embed(self, ctx, embed, url):

        newdata = {}

        if not os.path.exists('config') or not os.path.exists('config/record.json'):
            os.makedirs('config')
            data = {}
        elif os.path.exists('config/record.json'):
            with open('config/record.json', "r") as f:
                        data = json.load(f)

        newdata[ctx.guild.id] = {'blue_archive_news': url}

        if not value_exists(data, url):
            data.update(newdata)
        else:
            merge_dict(newdata, data)

        with open('config/record.json', "w") as f:
            json.dump(data, f, indent=4)

        await ctx.send(embed=embed)
    

async def setup(bot):
    await bot.add_cog(Task(bot))