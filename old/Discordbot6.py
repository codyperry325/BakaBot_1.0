import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
import random
import requests
import json
import aiohttp

#tenor addition
apikey= 'TR0SJ2RGME30'
lmt=15

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
    image= random.choice([ 'https://giphy.com/gifs/popeyeschicken-chicken-fried-biscuits-jqwk5Jxh8UcbMZbxK7','https://giphy.com/gifs/popeyeschicken-chicken-fried-biscuits-IeWbqFs6WX6IetZCKO', 'https://giphy.com/gifs/dennysdiner-club-chicken-8mvR8IAQsK4G32pRYd', 'https://giphy.com/gifs/5nsiFjdgylfK3csZ5T', 'https://giphy.com/gifs/trump-consequences-NTur7XlVDUdqM' ])
    await ctx.send(image)

#member join --needs work
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(837337386983096401)
    #guild=member.guild
    print(f'{member} joined boop')
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
async def inspire(ctx, inspirer=None):
    await ctx.send(ctx.message.author.mention + ' tries to inspire ' + inspirer)
    quote= random.choice(['https://giphy.com/gifs/black-and-white-life-britney-spears-qlibHBuiJV9S0', 'https://giphy.com/gifs/studiosoriginals-domitille-collardey-l41Yh1olOKd1Tgbw4', 'https://giphy.com/gifs/luck-good-im-rooting-for-you-12XDYvMJNcmLgQ', 'https://giphy.com/gifs/reaction-wRfVij0ow9h28'])
    await ctx.send(quote)

@bot.command()
async def wideputin(ctx):
    await ctx.send('WIDE PUTIN >:D')
    await ctx.send('https://www.youtube.com/watch?v=Wl959QnD3lM')
    
@bot.command()
async def website(ctx):
    await ctx.send('https://boopfc.weebly.com/')

#commands to add
#sus slapp do msq noskip pepep garly playdead doot

@bot.command()
async def sus(ctx, red=None):
    await ctx.send(ctx.message.author.mention + ' thinks ' + red + ' is sus ')
    suspect= random.choice(['https://giphy.com/gifs/cat-meow-suspicious-xULW8hrrGJbixeGfCw', 'https://giphy.com/gifs/thefactoryvideo-the-factory-paolofilmmaker-paolo-santamaria-Huo7qbHGNnXUVoRYL9', 'https://giphy.com/gifs/GetPartiful-among-us-imposter-game-ysiCYZUJkW3XRb7k9K', 'https://giphy.com/gifs/video-game-among-us-computer-z3ZzHIN66i7X6KAbxh' ])
    await ctx.send(suspect)

@bot.command()
async def slapp(ctx, slapped=None):
    async with aiohttp.ClientSession() as session:
        embed = discord.Embed (
            title = 'SLAPP',
            description = "GET SLAPPED!",
            colour = discord.Colour.blue())

        search_term=('anime slap')
        response=await session.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))
        data= json.loads(await response.text())
        gif_choice=random.randint(0, 10)
        embed.set_image(url=data['results'][gif_choice]['media'][0]['gif']['url'])

        await session.close()
        await ctx.send(embed=embed)

bot.run(token)