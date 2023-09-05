import disnake
from typing import Optional
from Dbot import bot

class newbieconfirm(disnake.ui.View):
    def __init__(self, new_member_id):
        super().__init__(timeout=None)
        self.value = Optional[bool]
        # self.confirm_view = confirm_view  
        self.new_member = bot.get_user(new_member_id)
        self.new_member_id = self.new_member.id

    @disnake.ui.button(label="Принять", style=disnake.ButtonStyle.green, emoji="✔️")
    async def newbieconfirm(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        global newmember

        guild = bot.get_guild(1117027821827670089)

        new_member_guild = guild.get_member(int(self.new_member_id))

        role_first = guild.get_role(1117027821827670095)
        role_temp = guild.get_role(1118848120806178877)

        await new_member_guild.add_roles(role_first)
        await new_member_guild.add_roles(role_temp)

        channelnewbie = bot.get_channel(int(1118583261824815236))

        embed = disnake.Embed(
            title="Новый игрок!",
            description=(
                f"Игрок <@{self.new_member_id}> присоединяется к нам!\n"
                "Хорошей игры!\n"
            ),
            color=0x00a2ff
        )
        
        # # Выдача роли
        # role = disnake.utils.get(inter.guild.roles, name="Новый участник")
        # await newmember.add_roles(role)
        
        await channelnewbie.send(embed=embed, delete_after=30)
        await inter.response.send_message(f"<@{self.new_member_id}>, присоединяется к нам!")
        self.value = True
        self.stop()

    @disnake.ui.button(label="Отказать", style=disnake.ButtonStyle.red, emoji="👎")
    async def newbiecancel(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        channelnewbie = bot.get_channel(int(1118583261824815236))
        embed = disnake.Embed(
            title="Отказ в заявке",
            description=(
                f"Игроку <@{self.new_member_id }> было отказано в проходе!\n"
                "Попытай удачу снова через время!"
            ),
            color=0x00a2ff
        )
        
        await inter.response.send_message(f"<@{self.new_member_id }>, отказано в проходе к нам!", delete_after=30)
        await channelnewbie.send(embed=embed)
        self.value = False
        self.stop()

