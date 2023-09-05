import disnake
from disnake.ext import commands
from Dbot import bot
from Dbot_Requests_Folder.request_send_button import Confirm

class Bot_testf(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(guild_ids=[1097125882876923954])
    async def embedbutton(inter):
        view = Confirm()
        channel = bot.get_channel(int(1118583261824815236))
        button_embed = disnake.Embed(
            title="Новый способ писать заявки!",
            description="Если бот в сети, то вам для написания заявки нужно нажать кнопку **✍️Заявка**",
            color=0x03fc6b
        )

        await channel.send(embed=button_embed, view = view)

    
