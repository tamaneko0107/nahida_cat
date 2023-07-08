from discord.ext import commands

def setup(bot: commands.Bot):
    @bot.event
    async def on_message(mes):
        # 檢查訊息是否為指令
        if mes.content.startswith('^^test'):
            # 刪除訊息
            await mes.delete()
        await bot.process_commands(mes)