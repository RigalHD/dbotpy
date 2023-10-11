from disnake.ext import commands
from Dbot import bot
import disnake
from disnake import TextInputStyle


class EmbModal(disnake.ui.Modal):
    def __init__(self, channel, color, list_of_choices):
        self.channel = channel
        self.color = color
        self.emb_list = []
        # self.img_enable = False
        # self.enable_author = False
        self.list_of_choice = list_of_choices
        self.img_enable = disnake.ui.TextInput(
                label="Картинка",
                placeholder="Вставь сюда ссылку на картинку",
                custom_id="img_link",
                style=TextInputStyle.paragraph,
                max_length=3000,
            )
        self.author_ava = disnake.ui.TextInput(
                label="Аватарка автора",
                placeholder="Вставь сюда ссылку на аватарку, если она есть",
                custom_id="author_img_link",
                style=TextInputStyle.paragraph,
                max_length=3000,
            )
        self.author_name = disnake.ui.TextInput(
                label="Имя автора",
                placeholder="Введи имя автора",
                custom_id="author_name",
                style=TextInputStyle.paragraph,
                max_length=100,
            )


        self.components_emb= [
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
        if self.list_of_choice[0] == True:
            self.components_emb.append(self.img_enable)

        if self.list_of_choice[1] == True:
            self.components_emb.append(self.author_ava)
            self.components_emb.append(self.author_name)

        super().__init__(
            title="Эмбед",
            custom_id="create_embed",
            components=self.components_emb,
        )
    
    async def callback(self, inter: disnake.ModalInteraction):
        for key, value in inter.text_values.items():
            self.emb_list.append(value)
        print(self.img_enable)
        self.embed = disnake.Embed(
            title=self.emb_list[0],
            description=self.emb_list[1],
            color=self.color
            )
        if self.img_enable in self.components_emb:
            try:
                self.embed.set_image(url=self.emb_list[2])
            except disnake.errors.HTTPException:
                modal_user = bot.get_user(int(inter.user.id))
                await modal_user.send("При создании эмбеда возникла ошибка с ссылкой на картинку. Убедитесь, что ссылка верна")
                return
        if self.author_ava in self.components_emb and self.author_name in self.components_emb:
            print(self.emb_list)
            if self.img_enable in self.components_emb:
                print(self.emb_list[4], self.emb_list[3])
                self.embed.set_author(
                    name = self.emb_list[4],
                    icon_url=self.emb_list[3],
                )
            elif self.img_enable not in self.components_emb:
                self.embed.set_author(
                    name = self.emb_list[3],
                    icon_url=self.emb_list[2],
                )               
            
        await self.channel.send(embed=self.embed)
        await inter.response.send_message(f"Эмбед отправлен!", ephemeral=True)

# class EmbModal_img(disnake.ui.Modal):
#     def __init__(self, channel, color):
#         self.channel = channel
#         self.color = color
#         self.emb_list = []
#         global components_emb
#         components_emb= [
#             disnake.ui.TextInput(
#                 label="Название",
#                 placeholder="Название эмбеда",
#                 custom_id="название",
#                 style=TextInputStyle.short,
#                 max_length=100,
#             ),
            
#             disnake.ui.TextInput(
#                 label="Описание",
#                 placeholder="Описание эмбеда",
#                 custom_id="описание",
#                 style=TextInputStyle.paragraph,
#                 max_length=3000,
#             ),
#             disnake.ui.TextInput(
#                 label="Картинка",
#                 placeholder="Вставь сюда ссылку на картинку",
#                 custom_id="img_link",
#                 style=TextInputStyle.paragraph,
#                 max_length=3000,
#             ),
#         ]
#         super().__init__(
#             title="Эмбед",
#             custom_id="create_embed_img",
#             components=components_emb,
#         )
    
#     async def callback(self, inter: disnake.ModalInteraction):
#         for key, value in inter.text_values.items():
#             self.emb_list.append(value)

#         embed = disnake.Embed(
#             title=self.emb_list[0],
#             description=self.emb_list[1],
#             color=self.color
#             )
#         try:
#             embed.set_image(url=self.emb_list[2])
#             await self.channel.send(embed=embed)
#             await inter.response.send_message(f"Эмбед отправлен!", ephemeral=True)
#         except disnake.errors.HTTPException:
#             modal_user = bot.get_user(int(inter.user.id))
#             await modal_user.send("При создании эмбеда возникла ошибка с ссылкой на картинку. Убедитесь, что ссылка верна")
#             return
