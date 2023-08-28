import disnake
from disnake.ext import commands
from Dbot import bot
import sqlite3

class Bot_Requests_DB_Control(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(guild_ids=[1097125882876923954])
    async def clear_requests_db(inter: disnake.CommandInteraction):
        with sqlite3.connect("no_access_to_requests.db") as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM requests_to_server")
            db.commit()
            print(f"База данных очищена! -> {inter.user.id} ")
            await inter.send("База данных очищена!")
    

    