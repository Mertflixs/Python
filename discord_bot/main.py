import discord
from discord.ext import commands
from music import music

cogs = [music]

client = commands.bot(command_prefix = '?', intents = discord.Intents.all())

for i in range(len(cogs)):
	cogs[i].setup(client)

client.run("MTAzMjIyMzM1Mzg5OTA3MzU0Ng.GX-IIt.ZIuzdGFL-JlDkwyJgo4VE49fuWTptJ50wknsww")