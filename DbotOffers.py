from typing import Optional
import disnake
from disnake.ext import commands
from disnake import TextInputStyle
from disnake.interactions import MessageInteraction
from Dbot import bot


class Bot_Offers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[1097125882876923954])
    async def offernotanon(inter):
        view = OfferButton()
        channel = bot.get_channel(int(1102629280615252029))
        button_embed = disnake.Embed(
            title="Напиши предложение для нашей школы!",
            description='Если бот в сети, то ты можешь написать предложение президенту школы используя кнопку "Предложить" ',
            color=0x03fc6b
        )
        
        await channel.send(embed=button_embed, view = view)

    @commands.slash_command(guild_ids=[1097125882876923954])
    async def offeranon(inter):
        view = OfferButton()
        channelanon = bot.get_channel(int(1102629326236684338))
        button_embed = disnake.Embed(
            title="Напиши анонимное предложение для нашей школы!",
            description='Если бот в сети, то ты можешь написать анонимное предложение президенту школы используя кнопку "Предложить" ',
            color=0x03fc6b
        )
        
        await channelanon.send(embed=button_embed, view = view)


class OffersModal(disnake.ui.Modal):
    def __init__(self):
        global components_offers
        components_offers = [
            disnake.ui.TextInput(
                label="Опиши своё предложение",
                placeholder="Опиши своё предложение максимально подробно",
                custom_id="описаниe",
                style=TextInputStyle.paragraph,
                max_length=300,
            ),
            disnake.ui.TextInput(
                label="Оцени своё предложение",
                placeholder="?/10",
                custom_id="оценка",
                style=TextInputStyle.short,
                max_length=2,
            ),
        ]
        super().__init__(
            title="Напиши предложение",
            custom_id="create_offer",
            components=components_offers,
        )
    
    # global offerwriter
    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(
            title="Новое предложение",
            description=(f"<@{offerwriter}> написал предложение!"),
            color=0x8400ff
            )
        
        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            )
        
        authorbot = bot.get_user(581348510830690344)
        print(components_offers)
        await authorbot.send(embed=embed)
        await inter.response.send_message(f" <@{offerwriter}>, предложение отправлено!", delete_after=5)


class OfferButton(disnake.ui.View): 

    def __init__(self):
        super().__init__(timeout=None)
        self.value = Optional[bool]

    @disnake.ui.button(label="Предложить", style=disnake.ButtonStyle.green, emoji="✍️")
    async def offerbutt(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        self.value = True
        await inter.response.send_modal(modal=OffersModal())

    async def interaction_check(self, interaction: MessageInteraction):
        
        global offerwriter
        offerwriter = interaction.user.id

        return await super().interaction_check(interaction)