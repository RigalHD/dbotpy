import disnake
from disnake.ext import commands
from Dbot import bot
from Dbot_Embed_Folder.DropDowns import DropDownView


class For_Embed_Writing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[1097125882876923954], name = "fullembed")
    @commands.has_permissions(administrator=True)
    async def fullembed(ctx, name, description, embedauthor, iconauthorurl, authorurl, footertext, footericonurl, imageulr, channelid):
        channel = bot.get_channel(int(channelid))
        embedf=disnake.Embed(
            title=name,
            description=description,
            color=0x00a2ff,
        )
        embedf.set_author(
            name=embedauthor,
            url=authorurl,
            icon_url=iconauthorurl,
        )
        embedf.set_footer(
            text=footertext,
            icon_url=footericonurl,
        )
        embedf.set_image(url=imageulr)
        await channel.send(embed=embedf)


    @commands.slash_command(name = "embed")
    # @commands.slash_command(guild_ids=[1097125882876923954], name = "embed")
    @commands.has_permissions(administrator=True)
    async def embedmodal_(inter: disnake.CommandInteraction, channel: disnake.TextChannel):
        embed = disnake.Embed(
            title="Выбери цвет полоски эмбеда",
            description="Пока на выбор предоставляется пять цветов",
            color=0x00a2ff
        )
        
        await inter.send(embed=embed, view=DropDownView(channel), ephemeral=True, delete_after=20)

    # @commands.slash_command(name = "embed_img")
    # @commands.has_permissions(administrator=True)
    # async def embedmodal_img(inter: disnake.CommandInteraction, channel: disnake.TextChannel, color, img):
    #     if color.lower() == "синий":
    #         clr=0x00a2ff
            
    #     elif color.lower() == "красный":
    #         clr=0xff0000
            
    #     elif color.lower() == "зелёный":
    #         clr=0x135c19
            
    #     elif color.lower() == "жёлтый":
    #         clr=0xffff00

    #     elif color.lower() == "фиолетовый":
    #         clr=0x8400ff
        
    #     elif color.lower() == "чёрный":
    #         clr=0x000000
        
    #     elif color.lower() == "белый":
    #         clr=0xffffff

    #     await inter.response.send_modal(modal=For_Embed_Writing.EmbModal_img(channel, clr, img))

    # @commands.slash_command(name = "embed")
    # # @commands.slash_command(guild_ids=[1097125882876923954], name = "embed")
    # @commands.has_permissions(administrator=True)
    # async def embed(ctx, name, description, color: str, channel: disnake.TextChannel):
    #     # print(channel)    
    #     # channel2 = bot.get_channel(channel)
        
        # if color.lower() == "синий":
        #     clr=0x00a2ff
            
        # elif color.lower() == "красный":
        #     clr=0xff0000
            
        # elif color.lower() == "зелёный":
        #     clr=0x135c19
            
        # elif color.lower() == "жёлтый":
        #     clr=0xffff00

        # elif color.lower() == "фиолетовый":
        #     clr=0x8400ff
        
        # elif color.lower() == "чёрный":
        #     clr=0x000000
        
        # elif color.lower() == "белый":
        #     clr=0xffffff

        
    #     embed2=disnake.Embed(
    #         title=name,
    #         description=description,
    #         color=clr
    #         )

    #     await channel.send(embed=embed2)


#     @commands.slash_command(name = "user_personal_embed")
#     @commands.has_permissions(administrator=True)
#     async def user_personal_embed(inter: disnake.CommandInteraction):
#         embed = disnake.Embed(
#             title="Правила города NewSide",
#             description="""
# ## 1 • ДИСКОРД СЕРВЕР

# > **1.1** Веди себя уважительно ко всем
# > **1.2** Не мешай другим игрокам.
# > **1.3** Запрещён **18+** контент.
# > **1.4** Не беседуй на политические темы.

# ## 2 • ИГРОВОЙ ПРОЦЕСС

# > **2.1** Не убивай игроков и мобов.
# > **2.2** Запрет ношения брони (кроме ботинок), если у вас нет разрешения от администрации города. (пока можно только жителям, так как идет строительство)
# > **2.3** Не приноси в город динамит и т.п.
# > **2.4** Не воруй.
# > **2.5** Запрещено двойное гражданство
# > **2.6** Ты под инвизом? - это запрещено на нашей территории!
# > **2.7** Не ходи по запреткам.
#     """,
#             color=0x8400ff
#         )
#         embed.set_author(
#             name="NewSide",
#             icon_url=inter.guild.icon,
#         )
#         ch = bot.get_channel(int(1126137654724001862))

#         await ch.send(embed = embed)
