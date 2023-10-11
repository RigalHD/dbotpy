import disnake
from disnake import TextInputStyle
from Dbot import bot
import sqlite3
from Dbot_Requests_Folder.request_confirm_buttons import newbieconfirm

class MyModal(disnake.ui.Modal):
    def __init__(self):
        self.owner = bot.get_user(int(581348510830690344))
        self.new_member_data = []
        self.new_member_id = 0
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
            ),
            disnake.ui.TextInput(
                label="Чем на вы занимались на сервере до нас?",
                placeholder="Или ты - новичок на сервере?",
                custom_id="Твоё прошлое",
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
        
        self.new_member_id = inter.user.id
        new_member = bot.get_user(int(self.new_member_id))

        embed = disnake.Embed(
            title="Новая заявка",
            description=f"<@{self.new_member_id}> написал заявку! Принять или отказать?",
            color=0x00a2ff
            )
        

        with sqlite3.connect("no_access_to_requests.db") as db:
            cursor = db.cursor()

            cursor.execute(
                """CREATE TABLE IF NOT EXISTS requests_to_server(
                in_db_user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                discord_id BIGINT,
                nick TEXT,age INTEGER,
                play_time TEXT,
                past TEXT,
                p_status TEXT)"""
                )
            db.commit()


        vals = [self.new_member_id]

        for key, value in inter.text_values.items():
            vals.append(value)
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            )

        # vals.append("Test_status")

        with sqlite3.connect("no_access_to_requests.db") as db:
            cursor = db.cursor()
            
            cursor.execute("INSERT INTO requests_to_server(discord_id, nick, age, play_time, past) VALUES (?, ?, ?, ?, ?)", vals)
            db.commit()
            print("в базу данных внесена новая заявка!")
        
        ban_user = []
        with sqlite3.connect("no_access_to_requests.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT discord_id FROM requests_no_access")
            vf = cursor.fetchall()
            for value in vf:
                # print(value)

                ban_user.append(value)
                # print(ban_user)

            ban_user = [value[0] for value in vf]
            
            
            if self.new_member_id in ban_user:
                but_user = self.new_member_id
                cursor.execute("SELECT cause FROM requests_no_access WHERE discord_id = ?", (but_user,))
                fetch_reason = cursor.fetchone()
                reason = fetch_reason[0] if fetch_reason else "Спросите у администрации города"
                await inter.send(f"Вам запрещено отправлять заявку в данный город.\nПричина: {reason}", ephemeral=True)
                return
        
        
        await self.owner.send(embed=embed, view=newbieconfirm(self.new_member_id))
        await inter.response.send_message(f"<@{self.new_member_id}> заявка отправлена!", delete_after=5)
        await new_member.send(f"Твоя заявка на рассмотрении, <@{self.new_member_id}>")