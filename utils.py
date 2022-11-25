import random

import discord
import requests

from config import TENOR_API_KEY, TENOR_LIMIT


def create_embed(title, desc):
    embed = discord.Embed(title=title, description=desc,
                          colour=discord.Colour.blue())
    return embed


# search function


def gif_search(search_term: str):
    response = requests.get(
        f'https://g.tenor.com/v1/search?q={search_term}&key={TENOR_API_KEY}&limit={TENOR_LIMIT}'
    )
    if response.status_code != 200:
        raise Exception('Error returning gifs from Tenor.')
    data = response.json()
    gif_choice = random.randint(0, 10)
    url = data['results'][gif_choice]['media'][0]['gif']['url']
    return url


async def find_and_send_gif(ctx, embed_name: str, embed_message: str, search_term: str):
    embed = create_embed(
        embed_name, embed_message
    )

    try:
        url = gif_search(search_term)
        embed.set_image(url=url)
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f'Error getting gif from Tenor: {e}')


def special_number():
    number = random.randint(0, 99)
    return number