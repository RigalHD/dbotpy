from Dbot import bot
import disnake
from disnake.ext import commands
from DbotConfig import cens_words
from Dbot_Requests_Folder.request_send_button import Confirm
from DbotGymnasium36_Folder.DropDown36 import Menu_Button

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
            title="Отправь заявку на вступление к нам!",
            description="Если бот в сети, то вам для написания заявки нужно нажать кнопку **✍️Заявка**",
            color=0x03fc6b
        )

        await channel.send(embed=button_embed, view = view)



        view_menu_36= Menu_Button()
        channel_menu = bot.get_channel(int(1150855646133104722))
        await channel_menu.purge(limit=1)
        button_embed_report = disnake.Embed(
            title="Меню выбора",
            description='Чтобы выбрать то, что тебя интересует нажми кнопку "Меню"',
            color=0x03fc6b
        )
        
        await channel_menu.send(embed=button_embed_report, view = view_menu_36)
