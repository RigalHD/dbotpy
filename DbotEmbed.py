import disnake
from disnake.ext import commands
from Dbot import bot


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


    @commands.slash_command(guild_ids=[1097125882876923954], name = "embed")
    @commands.has_permissions(administrator=True)
    async def embed(ctx, name, description, color: str, channel):    
        channel2 = bot.get_channel(int(channel))
        
        if color.lower() == "синий":
            clr=hex(0x00a2ff)
            
        elif color.lower() == "красный":
            clr=0xff0000
            
        elif color.lower() == "зелёный":
            clr=0x135c19
            
        elif color.lower() == "жёлтый":
            clr=0xffff00

        elif color.lower() == "фиолетовый":
            clr=0x8400ff
        
        elif color.lower() == "чёрный":
            clr=hex(0x000000)
        
        elif color.lower() == "белый":
            clr=hex(0xffffff)

        
        embed2=disnake.Embed(
            title=name,
            description=description,
            color=clr
            )

        await channel2.send(embed=embed2)

    # @commands.slash_command(guild_ids=[1097125882876923954], name = "user_personal_embed")
    # @commands.has_permissions(administrator=True)
    # async def user_personal_embed(inter: disnake.CommandInteraction):
    #     embed = disnake.Embed(
    #         title="Предвыборная компания",
    #         description="Я - СтендПач и я кандидат на роль МИД. Ну в составе города ещё до открытия сервера и повидал многое. Появляюсь на сервере каждый день. Почему именно я, да потому что есть очень важный фактор в этой роли,что я знаю всех,и все знают меня. Также я в состоянии поднять нашу экономику с нуля,углубить лор нашего государства,поддерживать нейтралитет,обустроить западную Хайперлупу,создать пиар государство 'Коплис' и обеспечить популяризацию города тем,что сделаю реформы в испытательном сроке. С главами у меня все прекрасно,в частности с соседями,а именно с империей,расколом, АМК и Централом,ко всем остальным отношусь нейтрально",
    #         color=0x8400ff
    #     )
    #     embed.set_author(
    #         name="StandPuch",
    #         icon_url="https://media.discordapp.net/attachments/1069886045358915685/1135953351423574076/141_20230801181243.png?width=701&height=701",
    #     )
    #     ch = bot.get_channel(int(1135851122582634527))

    #     await ch.send(embed = embed)
        
