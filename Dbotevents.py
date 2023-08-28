from Dbot import bot
import disnake
from disnake.ext import commands
from DbotConfig import cens_words

class Bot_Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        await bot.process_commands(message)
        for content in message.content.split():
            for cens_word in cens_words:
                if content.lower() == "brook":
                    await message.delete()
                    await message.channel.send(f"брук лох")
                elif content.lower() == cens_word:
                    await message.delete()
                    await message.channel.send(f"**Как тебе не стыдно, **{message.author.mention}?")

    # @commands.Cog.listener()
    # async def on_command_error(self, message: disnake.Message):
    #     await message.channel.send("К сожалению с командой возникла ошибка!")
