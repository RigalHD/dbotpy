from typing import Optional
import disnake
from disnake.ext import commands
from disnake import TextInputStyle
from disnake.interactions import MessageInteraction
from Dbot import bot
import sqlite3

acs = 0

ban_users = [673943023247294504, 469043409525669891, 948234412896686202]

saved_message = None




class newbieconfirm(disnake.ui.View):
    def __init__(self, confirm_view):
        super().__init__(timeout=None)
        self.value = Optional[bool]
        self.confirm_view = confirm_view  # Сохраняем экземпляр Confirm

    @disnake.ui.button(label="Принять", style=disnake.ButtonStyle.green, emoji="✔️")
    async def newbieconfirm(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        global newmember

        buttnuser = self.confirm_view.buttnuser  # Получаем значение buttnuser из экземпляра Confirm
        guild = bot.get_guild(1117027821827670089)
        new_member = guild.get_member(int(buttnuser))
        role_first = guild.get_role(1117027821827670095)
        role_temp = guild.get_role(1118848120806178877)
        await new_member.add_roles(role_first)
        await new_member.add_roles(role_temp)
        channelnewbie = bot.get_channel(int(1118583261824815236))
        embed = disnake.Embed(
            title="Новый игрок!",
            description=(
                f"Игрок <@{buttnuser}> присоединяется к нам!\n"
                "Хорошей игры!\n"
            ),
            color=0x00a2ff
        )
        newmember = bot.get_user(int(buttnuser))
        
        # # Выдача роли
        # role = disnake.utils.get(inter.guild.roles, name="Новый участник")
        # await newmember.add_roles(role)
        
        await channelnewbie.send(embed=embed, delete_after=30)
        await inter.response.send_message(f"<@{buttnuser}>, присоединяется к нам!")
        self.value = True
        self.stop()

    @disnake.ui.button(label="Отказать", style=disnake.ButtonStyle.red, emoji="👎")
    async def newbiecancel(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        buttnuser = self.confirm_view.buttnuser  # Получаем значение buttnuser из экземпляра Confirm
        channelnewbie = bot.get_channel(int(1118583261824815236))
        embed = disnake.Embed(
            title="Отказ в заявке",
            description=(
                f"Игроку <@{buttnuser}> было отказано в проходе!\n"
                "Попытай удачу снова через время!"
            ),
            color=0x00a2ff
        )
        
        await inter.response.send_message(f"<@{buttnuser}>, отказано в проходе к нам!", delete_after=30)
        await channelnewbie.send(embed=embed)
        self.value = False
        self.stop()



class Confirm(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = Optional[bool]

    @disnake.ui.button(label="Заявка", style=disnake.ButtonStyle.green, emoji="✍️")
    async def confirm(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        self.value = True
        await inter.response.send_modal(modal=MyModal(self))
        # self.stop()

    async def interaction_check(self, interaction: MessageInteraction):
        return await super().interaction_check(interaction)


class MyModal(disnake.ui.Modal):
    def __init__(self, confirm_view):
        self.confirm_view = confirm_view  # Сохраняем экземпляр Confirm
        self.buttnuser = None  # Уникальная переменная для каждого модального окна
        components = [
            disnake.ui.TextInput(
                label="Ник в майнкрафте",
                placeholder="Ваш ник в майнкрафте",
                custom_id="Ник",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Ваш возраст",
                placeholder="Ваш реальный возраст",
                custom_id="Возраст",
                style=TextInputStyle.short,
            ),
            disnake.ui.TextInput(
                label="Сколько времени играете в майнкрафт?",
                placeholder="Сколько времени играете?",
                custom_id="Игровое время",
                style=TextInputStyle.paragraph,
            )
        ]
        super().__init__(
            title="Заявка на сервер",
            custom_id="emb_create",
            timeout=300,
            components=components,
        )

    async def callback(self, inter: disnake.ModalInteraction):
        view_instance = self.confirm_view  # Получаем экземпляр Confirm
        view_instance.buttnuser = inter.user.id  # Устанавливаем уникальную переменную buttnuser
        buttonuser = bot.get_user(int(view_instance.buttnuser))
        user = bot.get_user(int(581348510830690344))
        embed = disnake.Embed(title="Новая заявка", description=f"<@{view_instance.buttnuser}> написал заявку! Принять или отказать?", color=0x00a2ff)
        global acs
        a = []
        for key, value in inter.text_values.items():
            a.append(value)
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            )
        ban_user = []
        with sqlite3.connect("no_access_to_requests.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT discord_id FROM requests_no_access")
            vf = cursor.fetchall()
            for value in vf:
                # print(value)

                ban_user.append(value)
                # print(ban_user)
            
                # Извлекаем только значения из кортежей и создаем список пользователей с запретом
            ban_user = [value[0] for value in vf]
            
            
            if view_instance.buttnuser in ban_user:
                but_user = view_instance.buttnuser
                cursor.execute("SELECT cause FROM requests_no_access WHERE discord_id = ?", (but_user,))
                fetch_reason = cursor.fetchone()
                reason = fetch_reason[0] if fetch_reason else "Спросите у администрации города"
                await inter.send(f"Вам запрещено отправлять заявку в данный город.\nПричина: {reason}", ephemeral=True)
                return
        
        
        await user.send(embed=embed, view=newbieconfirm(view_instance))  # Создаем новый экземпляр Confirm для следующих заявок
        await inter.response.send_message(f"<@{view_instance.buttnuser}> заявка отправлена!", delete_after=5)
        await buttonuser.send(f"Твоя заявка на рассмотрении, <@{view_instance.buttnuser}>")





class Bot_testf(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.slash_command(guild_ids=[1097125882876923954, 1084069446051704844], name = "заявка")
    async def newembed(inter: disnake.AppCmdInter):
        """Напиши заявку!"""
        # global channelg, embedtitle
        # embedtitle = mdwembedtitle
        # global ctxus
        # ctxus = inter.user.id
        await inter.response.send_modal(modal=MyModal())

    @commands.slash_command(guild_ids=[1097125882876923954])
    async def embedbutton(inter):
        global saved_message
        view = Confirm()
        channel = bot.get_channel(int(1118583261824815236))
        button_embed = disnake.Embed(
            title="Новый способ писать заявки!",
            description="Если бот в сети, то вам для написания заявки нужно нажать кнопку **✍️Заявка**",
            color=0x03fc6b
        )

        saved_message = inter

        await channel.send(embed=button_embed, view = view)
    @commands.slash_command(guild_ids=[1097125882876923954, 1117027821827670089], name = "запрет_заявок")
    async def no_accses(inter: disnake.CommandInteraction, user: disnake.Member, cause):
        user_id = user.id
        with sqlite3.connect("no_access_to_requests.db") as db:
            cursor = db.cursor()

            cursor.execute("""CREATE TABLE IF NOT EXISTS requests_no_access(
                in_db_user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                discord_id BIGINT,
                cause TEXT
            )""")

            values = (user_id, cause)

            cursor.execute("INSERT INTO requests_no_access(discord_id, cause) VALUES (?, ?)", values)

            db.commit()
