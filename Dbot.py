import sqlite3
import disnake
from disnake.ext import commands

bot = commands.Bot(
    command_prefix="!!",
    help_command=None,
    activity=disnake.Game("NewSide"),
    intents=disnake.Intents.all(),
    status=disnake.Status.idle
    )


@bot.slash_command(name="аватарка")
async def user_avatar(inter: disnake.CommandInteraction, user: disnake.Member):
    avatar_url = user.avatar.url
    await inter.send(avatar_url)






@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")

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
async def calc(inter: disnake.CommandInteraction, a: int, oper: str, b: int):
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
async def ncalc(inter: disnake.CommandInteraction, x: int, z: int):
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


@bot.slash_command(guild_ids=[1051049677207912468], name="пропуска", description="Список людей, с доступом на территорию ГП")
async def propuski(inter: disnake.CommandInteraction):
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
async def ping(inter: disnake.CommandInteraction):
    await inter.response.send_message("Понг!")

@bot.slash_command(guild_ids=[1097125882876923954])
async def lscom(inter, titl, message, us):
    embedls = disnake.Embed(
        title=titl,
        description=message,
        color=0x00a2ff
    )

    user = bot.get_user(int(us))
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



# @bot.slash_command()
# async def send_r_message(inter: disnake.CommandInteraction):
#     global st_members
#     ch = bot.get_channel(int(1127221477427650621))
    
#     embed = disnake.Embed(
#         title="Как подать иск в суд?",
#         description="""
#     > **1.** Имя обвиняемого\n
#     > **2.** Причина подачи в суд (распишите все подробно)\n
#     > **3.** Что бы вы хотели получить в качестве компенсации?

#     """,
#         color=0x00a2ff
#     )

#     await ch.send(embed=embed)



