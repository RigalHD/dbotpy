from Dbot import bot
import disnake
from disnake.ext import commands
from DbotConfig import cens_words
from Dbot_Requests_Folder.request_send_button import Confirm

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

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot {bot.user} is ready to work!")
        channel = bot.get_channel(int(1118583261824815236))
        await channel.purge(limit=1)
        view = Confirm()
        button_embed = disnake.Embed(
            title="Новый способ писать заявки!",
            description="Если бот в сети, то вам для написания заявки нужно нажать кнопку **✍️Заявка**",
            color=0x03fc6b
        )

        await channel.send(embed=button_embed, view = view)
