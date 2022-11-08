import os

import discord
#from dotenv import load_dotenv
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

#bot command set up

bot = commands.Bot(command_prefix='#', intents=intents)

#token
#load_dotenv()
token = 'ODE3MTczNjM1OTU2ODY3MDgy.YEFqQQ.Aso1AU37qUg6jKMekr-8Lzodmko'

client = discord.Client()

#connection to the server

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print(bot.user.id)
    print(discord.__version__)
    print('-------')

#embed function

def create_embed(title, desc):
    embed = discord.Embed (
            title = title,
            description = desc,
            colour = discord.Colour.blue())
    return embed        

#search function

def gif_search(search_term):
    response=requests.get(f"https://g.tenor.com/v1/search?q={search_term}&key={apikey}&limit={lmt}")
    data= response.json()
    gif_choice=random.randint(0, 10)
    url=(data['results'][gif_choice]['media'][0]['gif']['url'])
    return url

##########################################################
#COMMANDS

#botcommand section
#boop
@bot.command()
async def boop(ctx, boopee=None):
    embed = create_embed('BOOP \o/', f'{ctx.message.author.mention} boops {boopee}\'s snoot')

    url=gif_search('anime boop')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

#addition
@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)
    print (left + right)

#fry
@bot.command()
async def fry(ctx, fry=None):
    embed = create_embed('TENDOS', f'{ctx.message.author.mention} deep fries {fry}')

    url=gif_search('tenders')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

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
    embed = create_embed('NAP TIME', f'{ctx.message.author.mention} wants to sleep!')

    url=gif_search('anime sleep')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

#hug
@bot.command()
async def hug(ctx, huggee=None):
    embed = create_embed('HUG <3', f'{ctx.message.author.mention} hugs {huggee}')

    url=gif_search('anime hug')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

#inspire
@bot.command()
async def inspire(ctx, inspirer=None):
    embed = create_embed('Inspireeeeee', f'{ctx.message.author.mention} inspires {inspirer}')

    url=gif_search('inspire')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def wideputin(ctx):
    embed = create_embed('WIDE PUTIN >:D', 'https://www.youtube.com/watch?v=Wl959QnD3lM')
    await ctx.send(embed=embed)
    #await ctx.send('WIDE PUTIN >:D')
    #await ctx.send('https://www.youtube.com/watch?v=Wl959QnD3lM')
    
@bot.command()
async def website(ctx):
    await ctx.send('https://boopfc.weebly.com/')

@bot.command()
async def sus(ctx, red=None):
   
    embed = create_embed('SUS', f'{ctx.message.author.mention} thinks {red} is sus!')

    url=gif_search('among us')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def slapp(ctx, slapped=None):
    
    embed = create_embed('slap', f'{ctx.message.author.mention} slaps {slapped}')

    url=gif_search('anime slap')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def mochi(ctx):
    embed = create_embed('CUTE', f'{ctx.message.author.mention} graces boop with adorbale cats')

    url=gif_search('mochi')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def nya(ctx):
    embed = create_embed('KITTY', f'{ctx.message.author.mention} graces boop with adorbale cats')

    url=gif_search('anime cat')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def pepep(ctx):
    embed = create_embed('PEPEP', f'{ctx.message.author.mention} wants a PEPEP')

    url=gif_search('soda dr. pepper')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def garly(ctx):

    embed = create_embed('GARLY', f'{ctx.message.author.mention} noms on some GARLY')

    url=gif_search('garlic bread')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def playdead(ctx):
    embed = create_embed('DETH >:D', f'{ctx.message.author.mention} plays dead for everyone')

    url=gif_search('anime dead')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def doot(ctx):
    embed = create_embed('DOOT', f'{ctx.message.author.mention} doots the songs of boop')

    url=gif_search('doot')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def catboi(ctx):
    embed = create_embed('GRAHA', f'{ctx.message.author.mention} wants to see the best cat boi')

    url=gif_search('graha tia')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def ascian(ctx):
    embed = create_embed('EMET <3', f'{ctx.message.author.mention} wants to see the best ascian')

    url=gif_search('emet selch')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def DOMSQ(ctx, msqer=None):
    embed = create_embed('MSQ', f'{ctx.message.author.mention} reminds {msqer} they need to do msq >:)')

    url=gif_search('anime slap')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

bot.run(token)