import disnake
from disnake.ext import commands
from typing import Optional
from Dbot_Requests_Folder.Requests_Modal import MyModal
from disnake.interactions import MessageInteraction


class Confirm(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Заявка", style=disnake.ButtonStyle.green, emoji="✍️")
    async def confirm(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        
        await inter.response.send_modal(modal=MyModal())
        # self.stop()

    # async def interaction_check(self, interaction: MessageInteraction):
    #     return await super().interaction_check(interaction)