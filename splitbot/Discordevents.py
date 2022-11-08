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
async def giveaway(ctx, hours : int, prize: str, host=None):
    embed = discord.Embed(title = "Giveaway time 🎉🎉🎉🎉🎉🎉🎉🎉", description = "Hey everyone, to enter the giveaway please click the reaction! Good luck to everyone <3", colour = discord.Colour.blue())

    end = datetime.datetime.now() + datetime.timedelta(seconds = hours*60*60)

    end_text = end.strftime("%H:%M, %x")

    if host == None:
        embed.add_field(name = "Prize", value = f"{prize}")
        embed.add_field(name = "Ends At:", value = f"{end_text} CST")
        embed.set_footer(text= f"Ends {hours} hours from now!")
    
    else:
        embed.add_field(name = "Prize", value = f"{prize}")
        embed.add_field(name = "Ends At:", value = f"{end_text} CST")
        embed.set_footer(text= f"Ends {hours} hours from now!")
        embed.add_field(name = "Prize Host", value = f"{host}")

    my_msg = await ctx.send(embed = embed)

    await my_msg.add_reaction("🎉")

    await asyncio.sleep(hours*60*60)

    new_msg = await ctx.channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await ctx.send(f"Congrats {winner.mention} you have won {prize}")

#glamour contest section 

@bot.command()
async def glamcontest(ctx, date: str,  time : str, theme : str):
    embed = discord.Embed(title = "Glamour Contest!!!", description = "It is time to get your glams ready :D Make sure to check the theme and have fun preparring your glam!")

    embed.add_field(name= "Date:", value=f"{date}")
    embed.add_field(name= "Time:", value=f"{time}")
    embed.add_field(name= "Theme:", value=f"{theme}")

    await ctx.send(embed=embed)

#general event 
@bot.command()
async def event(ctx, activity : str, date : str, time : str, descr : str):
    if activity == "Movie Night":
        embed = discord.Embed(title = 'Movie Night!!!! \o/', description = "Everyone get your popcorn and drinks ready for movie/anime night :)")

        embed.add_field(name="Date:", value=f"{date}")
        embed.add_field(name="Time:", value=f"{time}")
        embed.add_field(name="Movie:", value=f"{descr}")

        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title = f'{activity} \o/', description = f"{descr}")

        embed.add_field(name="Date:", value=f"{date}")
        embed.add_field(name="Time:", value=f"{time}")   

        await ctx.send(embed=embed)