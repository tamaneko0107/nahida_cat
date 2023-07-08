import discord
from discord.ext import commands
import json
import os
from core.bot_event import setup as setup_event

with open("setting.json",'r',encoding="utf8") as jset:
    setdata = json.load(jset)

intents= discord.Intents.all()
bot = commands.Bot(command_prefix="^^", intents=intents)

async def load_cog():
    for filename in os.listdir("./cmds"):
        if filename.endswith(".py"):
            extension_name = f"cmds.{filename[:-3]}"
            try:
                await bot.reload_extension(extension_name)
            except commands.ExtensionNotLoaded:
                await bot.load_extension(extension_name)

@bot.event
async def on_ready():
    channel = bot.get_channel(993457414236020776)
    await channel.send("準備できたよ！")

    # 載入所有指令程式檔案
    await load_cog()
    
    try:
        synced = await bot.tree.sync()
        print(f"Synced {synced} commands")
    except Exception as e:
        print("An error occurred while syncing: ", e)

@bot.hybrid_command(name="reload_all")
async def reload_all(ctx):
    await load_cog()
    await ctx.send("Reload all done.")

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

setup_event(bot)

if __name__ == "__main__":
    bot.run(setdata["TOKEN"])