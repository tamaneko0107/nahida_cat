import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, mes):
        # 檢查訊息是否為指令
        if mes.content.startswith('^^123'):
            # 刪除訊息
            await mes.delete()

async def setup(bot):
   await bot.add_cog(Event(bot))