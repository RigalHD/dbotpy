from typing import Optional
import disnake
from disnake.ext import commands
from disnake import TextInputStyle
from disnake.interactions import MessageInteraction

bot = commands.Bot(command_prefix="!!", help_command=None, activity=disnake.Game("Грибную Партию"),intents=disnake.Intents.all(), status=disnake.Status.idle)

cens_words = ["rtest", "hellowein", "таракан", "хуй", "хуй", "xуй", "xyй", "хyй", "hui", "brook"]
#specialcens_words = ["brook"]


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
async def rkick(inter, member: disnake.Member, *, reason="Нарушение правил."):
    await inter.send(f"чела {member.mention} кикнул {inter.author.mention}", delete_after=5) 
    await member.kick(reason=reason)
    await inter.message.delete()

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

@bot.slash_command(guild_ids=[1097125882876923954], name = "embed")
@commands.has_permissions(administrator=True)
async def embed(ctx, name, description, color, channel):
    
    channel2 = bot.get_channel(int(channel))
    if color.lower() == "синий":
        embed2=disnake.Embed(
        title=name,
        description=description,
        color=0x00a2ff
    )
        
    elif color.lower() == "красный":
        embed2=disnake.Embed(
        title=name,
        description=description,
        color=0xff0000
    )
        
    elif color.lower() == "зелёный":
        embed2=disnake.Embed(
        title=name,
        description=description,
        color=0x135c19
    )
        
    elif color.lower() == "жёлтый":
        embed2=disnake.Embed(
        title=name,
        description=description,
        color=0xffff00
    )
    
    elif color.lower() == "фиолетовый":
        embed2=disnake.Embed(
        title=name,
        description=description,
        color=0x8400ff
    )
    
    elif color.lower() == "чёрный":
        embed2=disnake.Embed(
        title=name,
        description=description,
        color=0x000000
    )
    
    elif color.lower() == "белый":
        embed2=disnake.Embed(
        title=name,
        description=description,
        color=0xffffff
    )
    
    await channel2.send(embed=embed2)

# @bot.slash_command()
# @commands.has_permissions(administrator=True)
# async def sent(inter, messag, c_id):
#     channelg = bot.get_channel(int(c_id))
#     await channelg.send(messag)


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

@bot.slash_command(guild_ids=[1097125882876923954])
async def voicedel(ctx, voice):
    vchannel = bot.get_channel(int(voice))
    await vchannel.delete()

@bot.slash_command(guild_ids=[1097125882876923954])
async def roleget(ctx, newmember = disnake.Member, *, gildd, rle):
    gild = bot.get_guild(int(gildd))
    role = gild.get_role(int(rle))
    await newmember.add_roles(role)



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
    await user.send("👀")
    await user.send(embed=embedls)

class MyModal(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Ник в майнкрафте",
                placeholder="Ваш ник в майнкрафте",
                custom_id="ваш ник",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Ник на атерносе",
                placeholder="Ваш ник на сайте atenos.org",
                custom_id="атернос",
                style=TextInputStyle.short,
            ),
            disnake.ui.TextInput(
                label="Ваш возраст",
                placeholder="Ваш реальный возраст",
                custom_id="возраст",
                style=TextInputStyle.short,
            ),
            disnake.ui.TextInput(
                label="Почему Вы хотите играть на нашем сервере?",
                placeholder="Почему?",
                custom_id="почему",
                style=TextInputStyle.paragraph,
            ),
            disnake.ui.TextInput(
                label="Что Вы будете делать?",
                placeholder="Чем будете заниматься?",
                custom_id="занятия",
                style=TextInputStyle.paragraph,
            )
        ]
        super().__init__(
            title="Заявка на сервер от",
            custom_id="emb_create",
            components=components,
        )

    async def callback(self, inter: disnake.ModalInteraction):
        global buttnuser
        view = newbieconfirm()
        buttonuser = bot.get_user(int(buttnuser[0]))
        user = bot.get_user(int(581348510830690344))
        # userwrote = bot.get_user(int(ctxus))
        embed = disnake.Embed(title="Новая заявка", description=f"<@{buttnuser[0]}> написал заявку! Принять или отказать?", color=0x00a2ff)
        # channelg = bot.get_channel(int(1101190863826210818))
        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            )
        # await user.send(embed=embed)
        # await user.send(f' <@{buttnuser}> написал заявку!')
        await user.send(embed=embed, view=view)
        # await user.send(f' <@{buttnuser}> написал заявку! Принять или отказать?', view=view)
        await inter.response.send_message(f"<@{buttnuser[0]}>, заявка отправлена!", delete_after=5)
        await buttonuser.send(f"Твоя заявка на рассмотрении, <@{buttnuser[0]}>")

# @bot.slash_command(guild_ids=[1097125882876923954, 1084069446051704844], name = "заявка")
# async def newembed(inter: disnake.AppCmdInter):
#     """Напиши заявку!"""
#     # global channelg, embedtitle
#     # embedtitle = mdwembedtitle
#     # global ctxus
#     # ctxus = inter.user.id
#     await inter.response.send_modal(modal=MyModal())


class newbieconfirm(disnake.ui.View):

    def __init__(self):
          super().__init__(timeout=None)
          self.value = Optional[bool]

    @disnake.ui.button(label="Принять", style=disnake.ButtonStyle.green, emoji="✔️")
    async def newbieconfirm(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        global newmember, buttnuser
        channelnewbie = bot.get_channel(int(1084084491255025694))
        embed = disnake.Embed(
              title="Новый игрок!",
              description=(
              f"Игрок <@{buttnuser[0]}> получил проходку на сервер!\n"
              "Хорошей игры на сервере!\n"
              ),
              color=0x00a2ff
           )
        newmember = bot.get_user(int(buttnuser[0]))
        # await newmember.get_role(role)
        # view = NewBieFinalConfirm()
        await channelnewbie.send(embed=embed)
        buttnuser.pop[0]
        # await newmember.send("Ты получаешь проходку на сервер! Нажми на кнопку для подтверждения входа!", view=view)
        await inter.response.send_message(f"<@{buttnuser[0]}>, получает проходку!")
        self.value = True
        self.stop()
    
    @disnake.ui.button(label="Отказать", style=disnake.ButtonStyle.red, emoji="👎")
    async def newbiecancel(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        global buttnuser
        channelnewbie = bot.get_channel(int(1084084491255025694))
        embed = disnake.Embed(
            title="Отказ в заявке",
            description=(
            f"Игроку <@{buttnuser[0]}> было отказано в проходе на сервер!\n"
            "Попытай удачу снова через время!"
            ),
            color=0x00a2ff
        )
        await inter.response.send_message(f"<@{buttnuser[0]}>, отказано в проходе на сервер!")
        await channelnewbie.send(embed=embed)
        buttnuser.pop[0]
        self.value = False
        self.stop()

class Confirm(disnake.ui.View): 

    def __init__(self):
        super().__init__(timeout=None)
        self.value = Optional[bool]

    @disnake.ui.button(label="Заявка", style=disnake.ButtonStyle.green, emoji="✍️")
    async def confirm(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        self.value = True
        await inter.response.send_modal(modal=MyModal())
        # self.stop()

    async def interaction_check(self, interaction: MessageInteraction):
        global buttnuser
        buttnuser = []
        buttnuser.append(interaction.user.id) 
        print(buttnuser[0,1,2,3])
        return await super().interaction_check(interaction)


@bot.slash_command()
async def embedbutton(inter):
    view = Confirm()
    channel = bot.get_channel(int(1084084491255025694))
    button_embed = disnake.Embed(
        title="Новый способ писать заявки!",
        description="Если бот в сети, то вам для написания заявки нужно нажать кнопку **✍️Заявка**",
        color=0x03fc6b
    )

    await channel.send(embed=button_embed, view = view)


#нужно дать возможность боту делать очередь из заявок!!!
#нужно дать возможность боту делать очередь из заявок!!!
#нужно дать возможность боту делать очередь из заявок!!!
#нужно дать возможность боту делать очередь из заявок!!!
#нужно дать возможность боту делать очередь из заявок!!!

@bot.slash_command(description="Тестовая команда для проверки работы команд")
async def bottestping(ctx, rol: disnake.Role):
    await ctx.send(rol.id)

@bot.slash_command(description="Тестовая команда для проверки работоспособности бота")
async def bottestroleinfo(ctx, member: disnake.Member, *, role: disnake.Role):
    # rle = disnake.Role(айди роли) команда для выдачи роли
    await member.add_roles(role)


@bot.slash_command(guild_ids=[1097125882876923954], name="reg", description="Регистарция")
async def registration(inter: disnake.CommandInteraction, yourname: str, forname: str, form: str):
    membernew = inter.user.id
    owner = bot.get_user(int(581348510830690344))
    newmembermention = bot.get_user(int(membernew))
    with open(r'C:\Users\meljn\users.txt', 'a+', encoding='utf-8') as userfile:
        userfile.write(f"{yourname} {forname} {form} {newmembermention} \n")
    await owner.send(f"{yourname} {forname} {form} <@{membernew}> \n")
    userfile.close()
    # with open(r'C:\Users\meljn\users.txt', 'r', encoding='utf-8') as userfilef:
    #     await user.send(userfilef.read()) 
    role = inter.guild.get_role(int(1101149791829889134))
    await inter.user.add_roles(role)
    userfile.close()

    















































































bot.run("MTA4ODQ3NzIwNTI5MTYwNjA4OA.G39TYp.rtpogLMClCmIl9OPOK3xhJzm5sCJbDsfbaFnBM")