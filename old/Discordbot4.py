import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
import random

intents=discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='#', intents=intents)

load_dotenv()
token = 'ODE3MTczNjM1OTU2ODY3MDgy.YEFqQQ.Aso1AU37qUg6jKMekr-8Lzodmko'

client = discord.Client()

#connection to the server

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print(bot.user.id)
    print(discord.__version__)
    print('-------')

#botcommand section
#boop
@bot.command()
async def boop(ctx, boopee=None):
    await ctx.send(ctx.message.author.mention + ' boops ' + boopee + "'s snoot")
    image= random.choice(['https://giphy.com/gifs/cat-daww-adorableness-10MSCF1viNV7zy', 'https://giphy.com/gifs/enjoy-luna-boops-FsFAxc5zMnVks', 'https://giphy.com/gifs/cute-aww-eyebleach-aCqb9YW7QclN3rtto5', 'https://giphy.com/gifs/lists-hSvBxxFsk0jhm'])
    await ctx.send(image)

#addition
@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)
    print (left + right)

#fry
@bot.command()
async def fry(ctx, fry=None):
    await ctx.send(ctx.message.author.mention + ' deep fries ' + fry)
    image= random.choice(['https://giphy.com/gifs/dennysdiner-club-chicken-8mvR8IAQsK4G32pRYd', 'https://giphy.com/gifs/fail-will-smith-fresh-prince-of-bel-air-12lL9jqB0Ogx2w', 'https://giphy.com/gifs/5nsiFjdgylfK3csZ5T', 'https://giphy.com/gifs/trump-consequences-NTur7XlVDUdqM' ])
    await ctx.send(image)

#member join --needs work
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(836984968977711114)
    #guild=member.guild
    print('yay')
    await channel.send(f'Welcome to BOOP {member}! Please be preparred to be BOOPED >:D')

#popcorn
@bot.command()
async def pop(ctx):
    await ctx.send(ctx.message.author.mention + ' eats some popcorn')
    await ctx.send('https://tenor.com/view/peach-cat-peach-and-goma-cute-gif-19880568')

#sleep
@bot.command()
async def sleep(ctx):
    await ctx.send(ctx.message.author.mention + ' wants to sleep')
    image= random.choice(['https://giphy.com/gifs/sleepy-yawn-iQHDtnUZ7gxI4', 'https://giphy.com/gifs/awwnime-TJNYHjqrgTGPm', 'https://giphy.com/gifs/sleepy-anime-girl-CoeFBrfvxzZ2U', 'https://giphy.com/gifs/sleep-tired-sleeping-142TwXbDJSAweY' ])
    await ctx.send(image)

#hug
@bot.command()
async def hug(ctx, huggee=None):
    await ctx.send(ctx.message.author.mention + ' gives ' + huggee + ' a big hug!')
    image= random.choice(['https://giphy.com/gifs/PHZ7v9tfQu0o0', 'https://giphy.com/gifs/happy-hug-od5H3PmEG5EVq', 'https://giphy.com/gifs/anime-boy-LIqFOpO9Qh0uA', 'https://giphy.com/gifs/fullmetal-alchemist-funny-anime-cute-HaC1WdpkL3W00'])
    await ctx.send(image)

#inspire
@bot.command()
async def inspire(ctx, inspirer):
    await ctx.send(ctx.message.author.mention + ' tries to inspire ' + inspirer)
    quote= random.choice(['https://giphy.com/gifs/black-and-white-life-britney-spears-qlibHBuiJV9S0', 'https://giphy.com/gifs/studiosoriginals-domitille-collardey-l41Yh1olOKd1Tgbw4', 'https://giphy.com/gifs/luck-good-im-rooting-for-you-12XDYvMJNcmLgQ', 'https://giphy.com/gifs/reaction-wRfVij0ow9h28'])
    await ctx.send(quote)

bot.run(token)