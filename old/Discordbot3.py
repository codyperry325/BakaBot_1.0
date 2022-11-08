import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
import random



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

#botcommand section
@bot.command()
async def boop(ctx, boopee=None):
    await ctx.send(ctx.message.author.mention + ' boops ' + boopee + "'s snoot")

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)
    print (left + right)

@bot.command()
async def fry(ctx, fry=None):
    await ctx.send(ctx.message.author.mention + ' deep fries ' + fry)
    iamge= random.choice(['https://giphy.com/gifs/fail-will-smith-fresh-prince-of-bel-air-12lL9jqB0Ogx2w', 'https://giphy.com/gifs/5nsiFjdgylfK3csZ5T', 'https://giphy.com/gifs/trump-consequences-NTur7XlVDUdqM' ])
    await ctx.send(image)


@bot.event
async def on_member_join(member):
    await channel.send('welcome ' +member )
    image= random.choice()

@bot.command()
async def pop(ctx):
    await ctx.send(ctx.message.author.mention + ' eats some popcorn')
    await ctx.send('https://tenor.com/view/peach-cat-peach-and-goma-cute-gif-19880568')

@bot.command()
async def sleep(ctx):
    await ctx.send(ctx.message.author.mention + ' wants to sleep')
    image= random.choice(['https://giphy.com/gifs/sleepy-yawn-iQHDtnUZ7gxI4', 'https://giphy.com/gifs/awwnime-TJNYHjqrgTGPm', 'https://giphy.com/gifs/sleepy-anime-girl-CoeFBrfvxzZ2U', 'https://giphy.com/gifs/sleep-tired-sleeping-142TwXbDJSAweY' ])
    await ctx.send(image)


bot.run(token)