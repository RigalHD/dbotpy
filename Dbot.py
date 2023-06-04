import sqlite3
from typing import Optional
import disnake
from disnake.ext import commands
from disnake import TextInputStyle
from disnake.interactions import MessageInteraction

bot = commands.Bot(
    command_prefix="!!", help_command=None,
    activity=disnake.Game("Грибную Партию"),
    intents=disnake.Intents.all(),
    status=disnake.Status.idle
    )

@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")
    
cens_words = ["rtest", "hellowein", "таракан", "хуй", "хуй", "xуй", "xyй", "хyй", "hui", "brook"]

# @bot.event
# async def on_member_join(member):
#     #role = await disnake.utils.get(member.guild.roles, id=1090000650512912414) 
#     channel = bot.get_channel(1051049678285840386) #member.guild.system_channel

#     embed = disnake.Embed(
#         title="Новый участник!", 
#         description=f"{member.name}#{member.discriminator}, Добро пожаловать!",
#         color=0x00ff5e
#     )
    
#     #await member.add_roles(role)
#     await channel.send(embed=embed)



# @bot.event
# async def on_command_error(inter: disnake.CommandInteraction, error: disnake):
#     print(error)

#     if isinstance(error, commands.MissingPermissions):
#         await inter.send(f"{inter.author}, у тебя нет прав")
#     elif isinstance(error, commands.UserInputError):
#         await inter.send(embed=disnake.Embed(
#             title="Как писать команду *правильно?*",
#             description=f" '{inter.application_command}' Example: /kick @klauncher заколебал",
#             color=0x0066ff 
#         ))


@bot.command(name="rmessage")
@commands.has_permissions(administrator=True)
async def rmessage(ctx: disnake.Interaction, tl, ms):
    # l=a.split("/")
    await ctx.send(embed=disnake.Embed(
        title=tl,
        description=ms,
        color=0x00a2ff
    ))

@bot.slash_command()
@commands.has_permissions(administrator=True)
async def rkick(inter: disnake.CommandInteraction, member: disnake.Member, *, reason="Нарушение правил."):
    await inter.send(f"чела {member.mention} кикнул {inter.author.mention}", delete_after=5) 
    await member.kick(reason=reason)
    await inter.delete_original_message()

@bot.slash_command()
async def calc(inter: disnake.Interaction, a: int, oper: str, b: int):
    if oper == "+":
        result = a + b
    elif oper == "-":
        result = a - b
    elif oper == "*" or oper == "x":
        result = a * b
    elif oper == "/" or oper == ":":
        result = a / b
    else:
        result = "нет"

    await inter.send(str(result))

@bot.slash_command(description="Рассчитает ваши координаты в аду")
async def ncalc(inter: disnake.Interaction, x: int, z: int):
    x_nether = round(x / 8)
    z_nether = round(z / 8)
    result = (f"x = {x_nether} | z = {z_nether}") 

    await inter.send(embed=disnake.Embed(
        title="Координаты по аду:",
        description=result,
        color=0x0066ff
    ))

@bot.slash_command(guild_ids=[1097125882876923954])
@commands.has_permissions(administrator=True)
async def msg(inter: disnake.CommandInteraction, msg, c_id):
    channelg = bot.get_channel(int(c_id))
    await channelg.send(msg)

# @bot.slash_command()
# async def samck(inter):


@bot.slash_command(guild_ids=[1051049677207912468, 889494053345968198], name="пропуска", description="Список людей, с доступом на территорию ГП")
async def propuski(inter: disnake.Interaction):
    embedspisok =  disnake.Embed(
        title="Список людей, у которых есть пропуск на территорию ГП",
        description=(
        "**meljnichenko** - бессрочно - член ГП  "
        "**\nStandPuch** - бессрочно - член ГП  "
        "**\nHellowein** - бессрочно - член ГП  "
        "**\nabjorka** - бессрочно - член ГП  "
        "**\nthetopir** - бессрочно - член ГП  "
        "**\nSas-Pido-ra-kin** - бессрочно - член ГП  "
        "**\nmr_KLauncher** - бессрочно - выдано Standpuch  "
        "**\nz1mp1e** - бессрочный пропуск - выдано StandPuch "
        ),   
        color=0x00a2ff
        )
    await inter.send(embed=embedspisok)

# @bot.slash_command()
# async def kickvoice(ctx, member: disnake.Member):
#     await member.voice.channel.delete

@bot.slash_command(guild_ids=[1097125882876923954], name = "fullembed")
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


@bot.slash_command(guild_ids=[1097125882876923954], name = "embed")
@commands.has_permissions(administrator=True)
async def embed(ctx, name, description, color: str, channel: int):    
    channel2 = bot.get_channel(channel)
    
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

@bot.slash_command(guild_ids=[1097125882876923954])
async def voicedel(inter: disnake.CommandInteraction, voice):
    vchannel = bot.get_channel(int(voice))
    await vchannel.delete()
    membernew = inter.user.id
    newmembermention = bot.get_user(int(membernew))
    with open(r'C:\Users\meljn\OneDrive\Документы\testbot\commandusers.txt', 'a+', encoding='utf-8') as userfile:
        userfile.write(f"использовал команду /voicedel : {newmembermention} \n")
    userfile.close()

@bot.slash_command()
async def ping(inter: disnake.Interaction):
    await inter.response.send_message("Понг!")

@bot.slash_command(guild_ids=[1097125882876923954])
async def lscom(inter, titl, message, us: int):
    embedls = disnake.Embed(
        title=titl,
        description=message,
        color=0x00a2ff
    )

    user = bot.get_user(us)
    await user.send(embed=embedls)

@bot.slash_command(description="Тестовая команда для проверки работы команд")
async def bottestping(ctx, rol: disnake.Role):
    print(rol.id)

@bot.slash_command(description="Тестовая команда для проверки работоспособности бота")
@commands.has_permissions(administrator=True)
async def bottestroleinfo(inter: disnake.CommandInteraction, member: disnake.Member, role: disnake.Role):
    await member.add_roles(role)
    membernew = inter.user.id
    newmembermention = bot.get_user(int(membernew))
    with open(r'C:\Users\meljn\OneDrive\Документы\testbot\commandusers.txt', 'a+', encoding='utf-8') as userfile:
        userfile.write(f"использовал команду для выдачи роли от лица бота : {newmembermention} \n")
    userfile.close()

@bot.slash_command(guild_ids=[1051049677207912468], name="репутация", description="Узнай сколько у тебя SocialCredit")
async def socialcredit(inter: disnake.CommandInteraction, member: disnake.Member):
    with sqlite3.connect("servertochka.db") as dbt:

        cursortochka = dbt.cursor()
        membermention = bot.get_user(int(member.id))
        mbr = str(member)
        cursortochka.execute('SELECT scredits FROM socialcredits WHERE ds_account = ?', (mbr,))
        result = cursortochka.fetchone()
        reputation = result[0] if result else 0
        results = f"Репутация **{membermention.mention}**: **{reputation}** SocialCredits"

        embed = disnake.Embed(
            title="Репутация",
            description=results,
            color=0x00a2ff
        )
        embed.set_author(
            name=f"{member.name}",
            icon_url=member.avatar.url
        )
        await inter.response.send_message(embed=embed)
        print(member)

# @bot.slash_command(guild_ids=[1051049677207912468], name="всярепутация", description="Узнай сколько у всех SocialCredit")
# async def socialcreditfull(inter: disnake.CommandInteraction):
#     with sqlite3.connect("servertochka.db")  as dbt:
#         cursortochka = dbt.cursor()
#         for value in cursortochka.execute("SELECT ds_account, scredits FROM socialcredits"):
#             await inter.send(value)
    
@bot.slash_command(guild_ids=[1097125882876923954])
@commands.has_permissions(administrator=True)
async def socialcreditset(inter, member: disnake.Member, credits: int):
    with sqlite3.connect("servertochka.db") as dbt:
        cursortochka = dbt.cursor()
        mbr = str(member)
        # values = (mbr, credits)
        global st_members
        cursortochka.execute("""CREATE TABLE IF NOT EXISTS socialcredits(
            in_db_user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ds_account TEXT,
            scredits BIGINT
        )""")
        # print(mbr)
        #Доделать
        # cursortochka.execute("INSERT INTO socialcredits(ds_account, scredits) VALUES (?, ?)", values)
        cursortochka.execute("UPDATE socialcredits SET scredits = ? WHERE ds_account = ?", (credits, mbr))

        # for i in st_members:
        #     values = (i, 0)
        #     cursortochka.execute("INSERT INTO socialcredits(ds_account, scredits) VALUES (?, ?)", values)

        dbt.commit()

        for value in cursortochka.execute("SELECT ds_account, scredits FROM socialcredits"):
            print(value)

@bot.slash_command(guild_ids=[1097125882876923954])
async def membrsofst(inter):
    global st_members
    st_members = []
    guild = bot.get_guild(int(1051049677207912468))
    for member in guild.members:
        st_members.append(str(member))

    print(st_members)
