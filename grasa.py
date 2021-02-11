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
from discord.ext import commands


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.listen()
async def on_message(msg):
    grasa = [":v", ":V", ">:v", ">:V", ':"v', ':"V', ":'v'", ":'V'", "7u7"]
    for word in grasa:
        if msg.content.count(word) > 0:
            await msg.channel.purge(limit=1)
            await msg.channel.send(f"amenaza eliminada")
    await bot.process_commands(msg)

bot.run(token=")
