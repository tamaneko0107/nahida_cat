import discord
from discord.ext import commands
import json
import os

with open("setting.json",'r',encoding="utf8") as jset:
    setdata = json.load(jset)

intents= discord.Intents.all()

bot = commands.Bot(command_prefix='^^', intents=intents)

@bot.event
async def on_ready():
    channel = bot.get_channel(993457414236020776)
    await channel.send("準備できたよ！")


    for filename in os.listdir("./cmds"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cmds.{filename[:-3]}")

# 載入指令程式檔案
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"Loaded {extension} done.")

# 卸載指令檔案
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"UnLoaded {extension} done.")

# 重新載入程式檔案
@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"ReLoaded {extension} done.")


if __name__ == "__main__":
    bot.run(setdata["TOKEN"])