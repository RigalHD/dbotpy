from disnake.ext import commands
import disnake
from disnake.ui import StringSelect, View
from Dbot_Embed_Folder.Modal_Classes_Embed import EmbModal, EmbModal_img

class DropDownView(View):
    def __init__(self, channel):
        self.channel = channel
        
        super().__init__()
        self.add_item(DropDown(self.channel))

class DropDown(StringSelect):
    def __init__(self, channel):
        self.channel = channel
        super().__init__(
            placeholder="Меню",
            max_values=1,
            min_values=1,
            options=[
                disnake.SelectOption(label="синий"),
                disnake.SelectOption(label="красный"),
                disnake.SelectOption(label="зелёный"),
                disnake.SelectOption(label="жёлтый"),
                disnake.SelectOption(label="фиолетовый")
            ]
        )

    async def callback(self, inter: disnake.MessageInteraction):
        if self.values[0] == "синий":
            clr=0x00a2ff

        elif self.values[0] == "красный":
            clr=0xff0000

        elif self.values[0] == "зелёный":
            clr=0x135c19   
                
        elif self.values[0] == "жёлтый":
            clr=0xffff00

        elif self.values[0] == "фиолетовый":
            clr=0x8400ff

        embed = disnake.Embed(
            title="Будет ли в эмбеде картинка?",
            description="Если выберешь \"Да\", то приготовь ссылку на картинку!",
            color=0x00a2ff
            )
        await inter.send(embed=embed, view=DropDownView_img(self.channel, clr), ephemeral=True, delete_after=20)


class DropDownView_img(View):

    def __init__(self, channel, color):
        self.channel = channel
        self.color = color
        
        super().__init__()
        self.add_item(DropDown_Img_Select(self.channel, color))

class DropDown_Img_Select(StringSelect):
    def __init__(self, channel, color):
        self.channel = channel
        self.clr = color
        super().__init__(
            placeholder="Меню",
            max_values=1,
            min_values=1,
            options=[
                disnake.SelectOption(label="Да"),
                disnake.SelectOption(label="Нет"),
            ]
        )

    async def callback(self, inter: disnake.MessageInteraction):
        if self.values[0] == "Да":
            await inter.response.send_modal(modal=EmbModal(self.channel, self.clr, True))

        elif self.values[0] == "Нет":
            await inter.response.send_modal(modal=EmbModal(self.channel, self.clr, False))
