import discord
from discord.ext import commands
from core.classes import Cog_Extension

def merge_dict(new, old={}):
    for key, value in new.items():
        if key in old and isinstance(old[key], dict) and isinstance(value, dict):
            merge_dict(value, old[key])
        else:
            old[key] = value

def value_exists(d, value):
    for k, v in d.items():
        if isinstance(v, dict):
            if value_exists(v, value):
                return True
        elif v == value:
            return True
    return False

class Main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{self.bot.latency*1000:.0f} ms')

async def setup(bot):
    await bot.add_cog(Main(bot))
