""""

┏━━━┓━━━━━┏┓━━━┏━━━┓━━━━━━━━━━━━━━━━━┏━━━┓━━┏━━━┓
┃┏━┓┃━━━━┏┛┗┓━━┃┏━┓┃━━━━━━━━━━━━━━━━━┃┏━┓┃━━┃┏━┓┃
┃┃━┃┃┏━┓━┗┓┏┛┏┓┃┃━┗┛┏━┓┏━━┓━┏━━┓┏━━┓━┗┛┏┛┃━━┃┃━┃┃
┃┗━┛┃┃┏┓┓━┃┃━┣┫┃┃┏━┓┃┏┛┗━┓┃━┃━━┫┗━┓┃━┏━┛┏┛━━┃┃━┃┃
┃┏━┓┃┃┃┃┃━┃┗┓┃┃┃┗┻━┃┃┃━┃┗┛┗┓┣━━┃┃┗┛┗┓┃┃┗━┓┏┓┃┗━┛┃
┗┛━┗┛┗┛┗┛━┗━┛┗┛┗━━━┛┗┛━┗━━━┛┗━━┛┗━━━┛┗━━━┛┗┛┗━━━┛
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Anti grasa 2.0, elimina la grasa de los servers de discord.

creado por IrregularDBJ#7373
discord.gg/JsddHWK

"""


import discord

class CLientGraso(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, msg):
        if msg.author == self.user:
            return
        
    async def on_message(self, msg):
    grasa = [":v", ":V", ">:v", ">:V", ':"v', ':"V', ":'v'", ":'V'", "7u7"]
    for word in grasa:
        if msg.content.count(word) > 0:
            await msg.channel.purge(limit=1)
            await msg.channel.send("amenaza eliminada")
            
bot = CLientGraso()
bot.run(token="")
