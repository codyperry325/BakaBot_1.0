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

@bot.command()
    async def movies(ctx, channel: get id):

        def filter_message(message):
            return '@' in message.content

        messages_in_channel = await channel.history(limit=15).map(filter_message).flatten()