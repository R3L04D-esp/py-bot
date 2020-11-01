import discord
from discord.ext import commands

client = commands.Bot(command_prefix='py!')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event 
async def on_member_join(member):
    print(f'{member} se ha unido al servidor.')

@client.event 
async def on_member_remove(member):
    print(f'{member} ha dejado el servidor.')

client.run('TOKEN')