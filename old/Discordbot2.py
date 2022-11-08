import os

import discord
from dotenv import load_dotenv
from discord.ext import commands



bot = commands.Bot(command_prefix='#')

load_dotenv()
token = 'ODE3MTczNjM1OTU2ODY3MDgy.YEFqQQ.Aso1AU37qUg6jKMekr-8Lzodmko'

client = discord.Client()

#connection to the server

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print(bot.user.id)
    print('-------')

#general messages section

#@client.event   
#async def on_message(message):
   #if message.author == client.user:
    #print(message)

    #if message.content.startswith('$hello'):
        #await message.channel.send('Hello!')
    
    #if message.content.startswith('$boop'):
        #to_boop = (f'boops the snoot of {parameter_name}')
        #await message.channel.send(to_boop)


#section to do booping
@bot.command()
async def boop(ctx, boopee=None):
    await ctx.send(ctx.message.author.mention + ' boops ' + boopee)

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)
    print (left + right)

@bot.command()
async def fry(ctx):
    await ctx.send('Deep fries some tendos')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel()
    await channel.send('welcome {member.name}')

bot.run(token)