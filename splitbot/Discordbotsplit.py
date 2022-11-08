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
from mytoken import API_KEY
from mytoken import DISCORD_TOKEN
import Discordmiscfunctions
import Discordcommands
import Discordevents

#tenor addition
apikey= API_KEY
lmt=11

intents=discord.Intents.default()
intents.members = True

#bot command set up

bot = commands.Bot(command_prefix=commands.when_mentioned_or('#'), intents=intents)

token = DISCORD_TOKEN

client = discord.Client()

#connection to the server

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print(bot.user.id)
    print(discord.__version__)
    print('-------')

bot.run(token) 