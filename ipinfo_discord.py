import discord
import re

client = discord.Client()

@client.event
async def on_ready():
  print("logged in as " + client.user.name)

@client.event
async def on_message(message):
#  if message.content == '8.8.8.8':
  if re.match('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',message.content):
    msg = message.author.mention + " Hi."
    await message.channel.send( msg)

client.run("NjEwMDM2MjE1MDcyMTYxODI1.XU_dBQ.9GaK3HZvdLrwQuzgIBpN1JYNRMQ")
