from collections import UserString
import os
from typing import Counter

import discord
from discord import embeds
from discord import colour
from discord import message
#from dotenv import load_dotenv
from discord.ext import commands
import random
import requests
import json
import aiohttp
import asyncio
import datetime

intents=discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or('#'), intents=intents)

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

#member join
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
async def slap(ctx, slapped=None):
    
    embed = create_embed('SLAPS >:D', f'{ctx.message.author.mention} slaps {slapped}')

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
    embed = create_embed('GRAHA <3', f'{ctx.message.author.mention} wants to see the best cat boi')

    url=gif_search('GrahaTia')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def ascian(ctx):
    embed = create_embed('EMET <3', f'{ctx.message.author.mention} wants to see the best ascian')

    url=gif_search('emetselch')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def domsq(ctx, msqer=None):
    if msqer == None:
        embed = create_embed('MSQ', f'{ctx.message.author.mention} reminds everyone that they need to do msq >:)')

        url=gif_search('anime slap')
        embed.set_image(url=url)
    else:
        embed = create_embed('MSQ', f'{ctx.message.author.mention} reminds {msqer} they need to do msq >:)')

        url=gif_search('anime slap')
        embed.set_image(url=url)   

    await ctx.send(embed=embed)

@bot.command()
async def dere(ctx):
    number=special_number()

    if number >=0 and number < 33:
        embed = create_embed('YANDERE', f'{ctx.message.author.mention} is a psycho Yandere :O')

        url=gif_search('yandere')
        embed.set_image(url=url)

        await ctx.send(embed=embed)
    
    if number >=33 and number < 66:
        embed = create_embed('Tsundere', f'{ctx.message.author.mention} doenst like you or anything BAKA!')

        url=gif_search('tsundere')
        embed.set_image(url=url)

        await ctx.send(embed=embed)

    if number >=66:
        embed = create_embed('Kudere', f'{ctx.message.author.mention} looks like a blank wall of unfeeling emotion')

        url=gif_search('Kudere')
        embed.set_image(url=url)

        await ctx.send(embed=embed)

@bot.command()
async def goodbot(ctx):
    embed = create_embed('Good Bot UwU', f'{ctx.message.author.mention} thinks baka bot is a good bot')

    url=gif_search('anime headpat')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def goodkaiyoko(ctx):
    embed = create_embed('Good Kaiyoko UwU', f'{ctx.message.author.mention} thinks Kaiyoko bot is a good bot')

    url=gif_search('anime headpat')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def hug(ctx, hugged=None):
    if hugged == None:
        embed = create_embed('Hugs <3', f'{ctx.message.author.mention} gives all boopers a hug')

        url=gif_search('anime hug')
        embed.set_image(url=url)
    else:
        embed = create_embed('Hugs <3', f'{ctx.message.author.mention} gives {hugged} a big hug')

        url=gif_search('anime hug')
        embed.set_image(url=url)   

    await ctx.send(embed=embed)

@bot.command()
async def lewd(ctx, lewdie=None):
    if lewdie == None:
        embed = create_embed('Lewdy >///<', f'{ctx.message.author.mention} is thinking mega lewd thoughts')

        url=gif_search('anime lewd')
        embed.set_image(url=url)
    else:
        embed = create_embed('Lewdy >///<', f'{ctx.message.author.mention} thinks {lewdie} is being super lewd')

        url=gif_search('anime lewd')
        embed.set_image(url=url)   

    await ctx.send(embed=embed)

@bot.command()
async def mehoy(ctx):
    embed = create_embed('MI HOY MINOY', f'{ctx.message.author.mention} graces chat with spongebob :)')

    url=gif_search('spongebob')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def blush(ctx):
    embed = create_embed('>////////////<', f'{ctx.message.author.mention} is suddenly really red')

    url=gif_search('anime blush')
    embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def owo(ctx, shocker = None):
    if shocker == None:
        embed = create_embed('OwO', f'{ctx.message.author.mention} is surprised OwO')

        url=gif_search('owo')
        embed.set_image(url=url)
    else:
        embed = create_embed('OwO', f'{ctx.message.author.mention} is surprised by {shocker} OwO')

        url=gif_search('owo')
        embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def kiss(ctx, kissed = None):
    if kissed == None:
        embed = create_embed('Kissy <3', f'{ctx.message.author.mention} sends everyone kisses')

        url=gif_search('Anime Kiss')
        embed.set_image(url=url)
    else:
        embed = create_embed('Kissy <3', f'{ctx.message.author.mention} kisses {kissed}')

        url=gif_search('owo')
        embed.set_image(url=url)

    await ctx.send(embed=embed)

@bot.command()
async def cry(ctx, cryee = None):
    if cryee == None:
        embed = create_embed(';w;', f'{ctx.message.author.mention} is crying')

        url=gif_search('anime cry')
        embed.set_image(url=url)
    else:
        embed = create_embed(';w;', f'{cryee} made {ctx.message.author.mention} cry')

        url=gif_search('anime cry')
        embed.set_image(url=url)

    await ctx.send(embed=embed)