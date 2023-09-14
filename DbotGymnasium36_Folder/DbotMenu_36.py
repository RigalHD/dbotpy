from typing import Optional
import disnake
from disnake.ext import commands
from Dbot import bot
from DbotGymnasium36_Folder.DropDown36 import Menu_Button


class Bot_Act_Menu_36(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[1097125882876923954])
    async def act_menu_36(inter):
        view = Menu_Button()
        channel_report = bot.get_channel(int(1150855646133104722))
        button_embed_report = disnake.Embed(
            title="Меню выбора",
            description='Чтобы выбрать то, что тебя интересует нажми кнопку "Меню"',
            color=0x03fc6b
        )
        
        await channel_report.send(embed=button_embed_report, view = view)
    