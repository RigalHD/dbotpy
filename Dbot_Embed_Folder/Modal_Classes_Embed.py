from disnake.ext import commands
from Dbot import bot
import disnake
from disnake import TextInputStyle


class EmbModal(disnake.ui.Modal):
    def __init__(self, channel, color):
        self.channel = channel
        self.color = color
        self.emb_list = []
        global components_emb
        components_emb= [
            disnake.ui.TextInput(
                label="Название",
                placeholder="Название эмбеда",
                custom_id="название",
                style=TextInputStyle.short,
                max_length=100,
            ),
            
            disnake.ui.TextInput(
                label="Описание",
                placeholder="Описание эмбеда",
                custom_id="описание",
                style=TextInputStyle.paragraph,
                max_length=3000,
            ),
        ]
        super().__init__(
            title="Эмбед",
            custom_id="create_embed",
            components=components_emb,
        )
    
    async def callback(self, inter: disnake.ModalInteraction):
        for key, value in inter.text_values.items():
            self.emb_list.append(value)

        embed = disnake.Embed(
            title=self.emb_list[0],
            description=self.emb_list[1],
            color=self.color
            )

        await self.channel.send(embed=embed)
        await inter.response.send_message(f"Эмбед отправлен!", ephemeral=True)

class EmbModal_img(disnake.ui.Modal):
    def __init__(self, channel, color):
        self.channel = channel
        self.color = color
        self.emb_list = []
        global components_emb
        components_emb= [
            disnake.ui.TextInput(
                label="Название",
                placeholder="Название эмбеда",
                custom_id="название",
                style=TextInputStyle.short,
                max_length=100,
            ),
            
            disnake.ui.TextInput(
                label="Описание",
                placeholder="Описание эмбеда",
                custom_id="описание",
                style=TextInputStyle.paragraph,
                max_length=3000,
            ),
            disnake.ui.TextInput(
                label="Картинка",
                placeholder="Вставь сюда ссылку на картинку",
                custom_id="img_link",
                style=TextInputStyle.paragraph,
                max_length=3000,
            ),
        ]
        super().__init__(
            title="Эмбед",
            custom_id="create_embed_img",
            components=components_emb,
        )
    
    async def callback(self, inter: disnake.ModalInteraction):
        for key, value in inter.text_values.items():
            self.emb_list.append(value)

        embed = disnake.Embed(
            title=self.emb_list[0],
            description=self.emb_list[1],
            color=self.color
            )
        try:
            embed.set_image(url=self.emb_list[2])
            await self.channel.send(embed=embed)
            await inter.response.send_message(f"Эмбед отправлен!", ephemeral=True)
        except disnake.errors.HTTPException:
            modal_user = bot.get_user(int(inter.user.id))
            await modal_user.send("При создании эмбеда возникла ошибка с ссылкой на картинку. Убедитесь, что ссылка верна")
            return
