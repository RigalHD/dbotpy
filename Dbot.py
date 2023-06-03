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

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    for content in message.content.split():
        for cens_word in cens_words:
            if content.lower() == "brook":
                await message.delete()
                await message.channel.send(f"брук лох")
            elif content.lower() == cens_word:
                await message.delete()
                await message.channel.send(f"**Как тебе не стыдно, **{message.author.mention}?")

# @bot.event
# async def on_command_error(inter, error):
#     print(error)

#     if isinstance(error, commands.MissingPermissions):
#         await inter.send(f"{inter.author}, у тебя нет прав")
#     elif isinstance(error, commands.UserInputError):
        # await inter.send(embed=disnake.Embed(
        #     title="Как писать команду *правильно?*",
        #     description=f" '{inter.prefix}{inter.command.name}' Example: /kick @klauncher заколебал",
        #     color=0x0066ff 
#         ))


@bot.command(name="rmessage")
@commands.has_permissions(administrator=True)
async def rmessage(ctx, tl, ms):
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
async def calc(inter, a: int, oper: str, b: int):
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
async def ncalc(inter, x: int, z: int):
    x_nether = round(x / 8)
    z_nether = round(z / 8)
    result = ("x = ", x_nether, "z = ", z_nether) 

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
async def propuski(inter):
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
async def embed(ctx, name, description, color, channel):    
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
async def ping(inter):
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
async def bottestroleinfo(inter: disnake.CommandInteraction, member: disnake.Member, *, role: disnake.Role):
    await member.add_roles(role)
    membernew = inter.user.id
    newmembermention = bot.get_user(int(membernew))
    with open(r'C:\Users\meljn\OneDrive\Документы\testbot\commandusers.txt', 'a+', encoding='utf-8') as userfile:
        userfile.write(f"использовал команду для выдачи роли от лица бота : {newmembermention} \n")
    userfile.close()



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

@bot.slash_command(guild_ids=[1097125882876923954])
async def offernotanon(inter):
    view = OfferButton()
    channel = bot.get_channel(int(1102629280615252029))
    button_embed = disnake.Embed(
        title="Напиши предложение для нашей школы!",
        description='Если бот в сети, то ты можешь написать предложение президенту школы используя кнопку "Предложить" ',
        color=0x03fc6b
    )
    
    await channel.send(embed=button_embed, view = view)

@bot.slash_command(guild_ids=[1097125882876923954])
async def offeranon(inter):
    view = OfferButton()
    channelanon = bot.get_channel(int(1102629326236684338))
    button_embed = disnake.Embed(
        title="Напиши анонимное предложение для нашей школы!",
        description='Если бот в сети, то ты можешь написать анонимное предложение президенту школы используя кнопку "Предложить" ',
        color=0x03fc6b
    )
    
    await channelanon.send(embed=button_embed, view = view)

@bot.slash_command(
        guild_ids=[1097125882876923954, 1102624788582760498],
        name="регистрация",
        description="Регистарция. Регистрацию можно проводить лишь раз"
        )
@commands.has_any_role(int(1104761162945527939))
async def registration(inter: disnake.CommandInteraction, имя: str, фамилия: str, класс: str):
    membernew = inter.user.id
    owner = bot.get_user(int(581348510830690344))
    newmembermention = bot.get_user(int(membernew))
    with open(r'C:\Users\meljn\OneDrive\Документы\testbot\users.txt', 'a+', encoding='utf-8') as userfile:
        userfile.write(f"{имя} {фамилия} {класс} {newmembermention} \n")
    await owner.send(f"{имя} {фамилия} {класс} <@{membernew}> \n")
    await inter.response.send_message(f"Успешная регистрация, <@{membernew}>!", delete_after=5)
    userfile.close()
    role_not_authorized = inter.guild.get_role(int(1104761162945527939))
    role_authorized = inter.guild.get_role(int(1104761018124619826))
    await inter.user.remove_roles(role_not_authorized)
    await inter.user.add_roles(role_authorized)
    userfile.close()

    values = (имя, фамилия, класс, 0, membernew)

    with sqlite3.connect("server.db") as db:
        cursor = db.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            in_db_user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT,
            login_forname TEXT,
            clas TEXT,
            cash BIGINT,
            discordaccountid BIGINT
        )""")

        cursor.execute("INSERT INTO users(login, login_forname, clas, cash, discordaccountid) VALUES (?, ?, ?, ?, ?)", values)

        db.commit()

        # cursor.execute('SELECT COUNT(*) FROM users WHERE login_forname = ?', (фамилия,))
        # result = cursor.fetchone()

        # Если количество найденных записей больше 0, значит имя уже существует в базе данных
        # if result[0] > 0:
        #     await inter.response.send_message('Фамилия уже есть в базе данных. Обратитесь в поддержку')
        # else:
        #     print('Имя не найдено в базе данных')

        for value in cursor.execute("SELECT * FROM users"):
            print(value)

@bot.slash_command(guild_ids=[1051049677207912468], name="репутация", description="Узнай сколько у тебя SocialCredit")
async def socialcredit(inter: disnake.CommandInteraction, member: disnake.Member):
    with sqlite3.connect("servertochka.db")  as dbt:

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
