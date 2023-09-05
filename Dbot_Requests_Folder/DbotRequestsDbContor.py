import disnake
from disnake.ext import commands
from Dbot import bot
import sqlite3

class Bot_Requests_DB_Control(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(guild_ids=[1097125882876923954])
    @commands.has_permissions(administrator=True)
    async def clear_requests_db(inter: disnake.CommandInteraction):
        with sqlite3.connect("no_access_to_requests.db") as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM requests_to_server")
            db.commit()
            print(f"База данных очищена! -> {inter.user.id} ")
            await inter.send("База данных очищена!")
    
    @commands.slash_command(guild_ids=[1097125882876923954], name="удалить_из_черного_списка")
    @commands.has_permissions(administrator=True)
    async def requests_no_accses_db_clear(inter: disnake.CommandInteraction, db_user_id):
        with sqlite3.connect("no_access_to_requests.db") as db:
            cursor = db.cursor()
            
            cursor.execute("DELETE FROM requests_no_access WHERE in_db_user_id = ? ", (db_user_id,))
            db.commit()

            print(f"В базе данных был очищен столбец с айди {db_user_id} ! -> {inter.user.id} ")
            await inter.send("Столбец очищен!")

    @commands.slash_command(guild_ids=[1097125882876923954, 1117027821827670089], name = "запрет_заявок")
    @commands.has_permissions(administrator=True)
    async def no_accses(inter: disnake.CommandInteraction, user: disnake.Member, cause):
        user_id = user.id
        with sqlite3.connect("no_access_to_requests.db") as db:
            cursor = db.cursor()

            cursor.execute("""CREATE TABLE IF NOT EXISTS requests_no_access(
                in_db_user_id INTEGERs PRIMARY KEY AUTOINCREMENT,
                discord_id BIGINT,
                cause TEXT
            )""")

            values = (user_id, cause)

            cursor.execute("INSERT INTO requests_no_access(discord_id, cause) VALUES (?, ?)", values)

            db.commit()


    