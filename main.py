import discord
from discord.ext import commands
import json

with open("setting.json",'r',encoding="utf8") as jset:
    setdata = json.load(jset)

bot = commands.Bot(command_prefix='^^')

@bot.event
async def on_ready():
    channel = bot.get_channel(993457414236020776)
    await channel.send("準備できたよ！")

@bot.command()
async def ping(ctx):
    await ctx.send(bot.latency)

bot.run(setdata["TOKEN"])