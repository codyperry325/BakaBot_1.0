# import argparse
import asyncio
import datetime
import random
import re

import discord
import utils

# from config import DISCORD_TOKEN
from discord.ext import commands

# parser = argparse.ArgumentParser(prog="khg-bot", description="khg-bot")
# parser.add_argument('-t', '--token', required=True)
# args = parser.parse_args()
# discord_token = args.token
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.messages = True

# bot command set up

bot = commands.Bot(command_prefix=commands.when_mentioned_or("#"), intents=intents)
client = discord.Client(intents=intents)
word_substitutions = utils.open_word_substitution_file()

# connection to the server


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")
    print(bot.user.id)
    print(discord.__version__)
    print(word_substitutions)
    print("-------")


# Bot Events

# member join


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(837337386983096401)
    # guild=member.guild
    print(f"{member} joined boop")
    await channel.send(
        f"Welcome to BOOP {member}! Please be preparred to be BOOPED >:D"
    )
    role = discord.utils.get(member.server.roles, id="<910606743204167771>")
    await bot.add_roles(member, role)


# on_message event listener


@bot.listen("on_message")
async def send_modified_message(message):
    if message.author != bot.user:
        message_contents = str(message.content)
        message_contents_split = message_contents.split(" ")
        made_substitution = False
        for word in message_contents_split:
            word = re.sub(r"[^a-zA-Z0-9 ]", "", word)
            if word in word_substitutions:
                message_contents = message_contents.replace(
                    word, word_substitutions[word.lower()]
                )
                made_substitution = True
        if made_substitution:
            await message.channel.send(message_contents, reference=message)


##########################################################
# COMMANDS#

# botcommand section
# boop
@bot.command()
async def boop(ctx, boopee=None):
    embed = utils.create_embed(
        "BOOP \\o/", f"{ctx.message.author.mention} boops {boopee}'s snoot"
    )

    url = utils.gif_search("anime boop")
    embed.set_image(url=url)

    await ctx.send(embed=embed)


# addition


@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)
    print(left + right)


# fry


@bot.command()
async def fry(ctx, fry=None):
    embed = utils.create_embed(
        "TENDOS", f"{ctx.message.author.mention} deep fries {fry}"
    )
    try:
        url = utils.gif_search("tenders")
        embed.set_image(url=url)

        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Error getting gif from Tenor: {e}")


# popcorn


@bot.command()
async def pop(ctx):
    await ctx.send(ctx.message.author.mention + " eats some popcorn")
    await ctx.send("https://tenor.com/view/peach-cat-peach-and-goma-cute-gif-19880568")


# sleep


@bot.command()
async def sleep(ctx):
    await utils.find_and_send_gif(
        ctx, "NAP TIME", f"{ctx.message.author.mention} wants to sleep!", "anime sleep"
    )


@bot.command()
async def inspire(ctx, inspirer=None):
    await utils.find_and_send_gif(
        ctx,
        "Inspireeeeee",
        f"{ctx.message.author.mention} inspires {inspirer}",
        "inspire",
    )


@bot.command()
async def wideputin(ctx):
    embed = utils.create_embed(
        "WIDE PUTIN >:D", "https://www.youtube.com/watch?v=Wl959QnD3lM"
    )
    await ctx.send(embed=embed)


@bot.command()
async def website(ctx):
    await ctx.send("https://boopfc.weebly.com/")


@bot.command()
async def sus(ctx, red=None):
    await utils.find_and_send_gif(
        ctx, "SUS", f"{ctx.message.author.mention} thinks {red} is sus!", "among us"
    )


@bot.command()
async def slap(ctx, slapped=None):
    await utils.find_and_send_gif(
        ctx, "SLAPS >:D", f"{ctx.message.author.mention} slaps {slapped}", "anime slap"
    )


@bot.command()
async def mochi(ctx):
    await utils.find_and_send_gif(
        ctx,
        "CUTE",
        f"{ctx.message.author.mention} graces boop with adorbale cats",
        "mochi",
    )


@bot.command()
async def nya(ctx):
    await utils.find_and_send_gif(
        ctx,
        "KITTY",
        f"{ctx.message.author.mention} graces boop with adorbale cats",
        "anime cat",
    )


@bot.command()
async def pepep(ctx):
    await utils.find_and_send_gif(
        ctx, "PEPEP", f"{ctx.message.author.mention} wants a PEPEP", "soda dr. pepper"
    )


@bot.command()
async def garly(ctx):
    await utils.find_and_send_gif(
        ctx, "GARLY", f"{ctx.message.author.mention} noms on some GARLY", "garlic bread"
    )


@bot.command()
async def playdead(ctx):
    await utils.find_and_send_gif(
        ctx,
        "DETH >:D",
        f"{ctx.message.author.mention} plays dead for everyone",
        "anime dead",
    )


@bot.command()
async def doot(ctx):
    await utils.find_and_send_gif(
        ctx, "DOOT", f"{ctx.message.author.mention} doots the songs of boop", "doot"
    )


@bot.command()
async def catboi(ctx):
    await utils.find_and_send_gif(
        ctx,
        "GRAHA <3",
        f"{ctx.message.author.mention} wants to see the best cat boi",
        "GrahaTia",
    )


@bot.command()
async def ascian(ctx):
    await utils.find_and_send_gif(
        ctx,
        "EMET <3",
        f"{ctx.message.author.mention} wants to see the best ascian",
        "emetselch",
    )


@bot.command()
async def domsq(ctx, msqer=None):
    if msqer is None:
        message = f"{ctx.message.author.mention} reminds everyone that they need to do msq >:)"
    else:
        message = (
            f"{ctx.message.author.mention} reminds {msqer} they need to do msq >:)"
        )

    await utils.find_and_send_gif(ctx, "MSQ", message, "anime slap")


@bot.command()
async def dere(ctx):
    number = utils.special_number()

    if number >= 0 and number < 33:
        embed_name = "YANDERE"
        message = f"{ctx.message.author.mention} is a psycho Yandere :O"
        search = "yandere"
    elif number >= 33 and number < 66:
        embed_name = "Tsundere"
        message = f"{ctx.message.author.mention} doenst like you or anything BAKA!"
        search = "tsundere"
    else:
        embed_name = "Kudere"
        message = (
            f"{ctx.message.author.mention} looks like a blank wall of unfeeling emotion",
        )
        search = "Kudere"

    await utils.find_and_send_gif(ctx, embed_name, message, search)


@bot.command()
async def goodbot(ctx):
    await utils.find_and_send_gif(
        ctx,
        "Good Bot UwU",
        f"{ctx.message.author.mention} thinks baka bot is a good bot",
        "anime headpat",
    )


@bot.command()
async def goodkaiyoko(ctx):
    await utils.find_and_send_gif(
        ctx,
        "Good Kaiyoko UwU",
        f"{ctx.message.author.mention} thinks Kaiyoko bot is a good bot",
        "anime headpat",
    )


@bot.command()
async def hug(ctx, hugged=None):
    if hugged is None:
        message = f"{ctx.message.author.mention} gives all boopers a hug"
    else:
        message = "Hugs <3", f"{ctx.message.author.mention} gives {hugged} a big hug"

    await utils.find_and_send_gif(ctx, "Hugs <3", message, "anime hug")


@bot.command()
async def lewd(ctx, lewdie=None):
    if lewdie is None:
        message = f"{ctx.message.author.mention} is thinking mega lewd thoughts"
    else:
        message = f"{ctx.message.author.mention} thinks {lewdie} is being super lewd"

    await utils.find_and_send_gif(ctx, "Lewdy >///<", message, "anime lewd")


@bot.command()
async def mehoy(ctx):
    await utils.find_and_send_gif(
        ctx,
        "MI HOY MINOY",
        f"{ctx.message.author.mention} graces chat with spongebob :)",
        "spongebob",
    )


@bot.command()
async def blush(ctx):
    await utils.find_and_send_gif(
        ctx,
        ">////////////<",
        f"{ctx.message.author.mention} is suddenly really red",
        "anime blush",
    )


@bot.command()
async def owo(ctx, shocker=None):
    if shocker is None:
        message = f"{ctx.message.author.mention} is surprised OwO"
    else:
        message = f"{ctx.message.author.mention} is surprised by {shocker} OwO"

    await utils.find_and_send_gif(ctx, "OwO", message, "owo")


@bot.command()
async def kiss(ctx, kissed=None):

    if kissed is None:
        message = f"{ctx.message.author.mention} sends everyone kisses"
        search_term = "Anime Kiss"
    else:
        message = f"{ctx.message.author.mention} kisses {kissed}"
        search_term = "owo"

    await utils.find_and_send_gif(ctx, "Kissy <3", message, search_term)


@bot.command()
async def cry(ctx, cryee=None):
    if cryee is None:
        message = f"{ctx.message.author.mention} is crying"
    else:
        message = f"{cryee} made {ctx.message.author.mention} cry"

    await utils.find_and_send_gif(ctx, ";w;", message, "anime cry")


@bot.command()
async def pout(ctx, pouter=None):
    if pouter is None:
        message = f"{ctx.message.author.mention} is pouting :T"

    else:
        message = f"{pouter} made {ctx.message.author.mention} pout :T"

    await utils.find_and_send_gif(ctx, "POUTY :T", message, "anime pout")


@bot.command()
async def lick(ctx, licked=None):
    if licked is None:
        message = f"{ctx.message.author.mention} is licking someone ;)"
    else:
        message = f"{ctx.message.author.mention} licks {licked}"

    await utils.find_and_send_gif(ctx, "Lick hehe~", message, "anime lick")


@bot.command()
async def michi(ctx):
    bot.get_channel(865635524140466216)
    await ctx.send("<@!512077737284861953>")
    await utils.find_and_send_gif(
        ctx,
        "Lewdy Supplier",
        f"{ctx.message.author.mention} summons the lewdy supplier to the lewdy corner UwU",
        "anime sexy",
    )


@bot.command()
async def duck(ctx):
    await utils.find_and_send_gif(
        ctx, "Ducks!", f"{ctx.message.author.mention} graces boop with Ducks :)", "duck"
    )


@bot.command()
async def happybirthday(ctx, birthdayboop=None):
    if birthdayboop is None:
        await ctx.send("Whose birthday is it silly?")
    else:
        await utils.find_and_send_gif(
            ctx,
            "HAPPY BIRTHDAY TO YOU <3",
            f"{ctx.message.author.mention} wishes {birthdayboop} a very special Happy Birthday! :D (and baka bot does too) ;)",
            "anime birthday",
        )


# lick,cuddle, confused

# GIVEAWAY SECTION


@bot.command()
async def giveaway(ctx, hours: int, prize: str, host=None):
    embed = discord.Embed(
        title="Giveaway time 🎉🎉🎉🎉🎉🎉🎉🎉",
        description="Hey everyone, to enter the giveaway please click the reaction! Good luck to everyone <3",
        colour=discord.Colour.blue(),
    )

    end = datetime.datetime.now() + datetime.timedelta(seconds=hours * 60 * 60)

    end_text = end.strftime("%H:%M, %x")

    if host is None:
        embed.add_field(name="Prize", value=prize)
        embed.add_field(name="Ends At:", value=f"{end_text} CST")
        embed.set_footer(text=f"Ends {hours} hours from now!")

    else:
        embed.add_field(name="Prize", value=prize)
        embed.add_field(name="Ends At:", value=f"{end_text} CST")
        embed.set_footer(text=f"Ends {hours} hours from now!")
        embed.add_field(name="Prize Host", value=host)
    await ctx.message.delete()
    await ctx.send("@everyone")
    my_msg = await ctx.send(embed=embed)

    await my_msg.add_reaction("🎉")

    await asyncio.sleep(hours * 60 * 60)

    new_msg = await ctx.channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await ctx.send(f"Congrats {winner.mention} you have won {prize}")


# glamour contest section


@bot.command()
async def glamcontest(ctx, date: str, time: str, theme: str):
    embed = discord.Embed(
        title="Glamour Contest!!!",
        description="It is time to get your glams ready :D Make sure to check the theme and have fun preparring your glam! @here",
    )

    embed.add_field(name="Date:", value=date)
    embed.add_field(name="Time:", value=time)
    embed.add_field(name="Theme:", value=theme)

    url = utils.gif_search("Fashion")

    embed.set_thumbnail(url=url)
    await ctx.message.delete()
    await ctx.send("@everyone")
    await ctx.send(embed=embed)


# general event


@bot.command()
async def event(ctx, activity: str, date: str, time: str, descr: str):
    if activity == "Movie Night":
        embed = discord.Embed(
            title="Movie Night!!!! \\o/",
            description="Everyone get your popcorn and drinks ready for movie/anime night :)",
        )

        embed.add_field(name="Date:", value=date)
        embed.add_field(name="Time:", value=time)
        embed.add_field(name="Movie:", value=descr)

        url2 = utils.gif_search("Movie Night")

        embed.set_thumbnail(url=url2)

        await ctx.message.delete()
        await ctx.send("@everyone")
        await ctx.send(embed=embed)

    elif activity == "Maps":
        embed = discord.Embed(
            title="Map Timeeeeeee!!! \\o/",
            description="Boooooops! It is time to plunder some gil and make us some money! Bring your two maps and your luck so we can get Ramuh to carry us to victory :)",
        )

        embed.add_field(name="Date:", value=date)
        embed.add_field(name="Time:", value=time)
        # embed.add_field(name="Map Type", value=f"{descr}")

        url2 = utils.gif_search("Maps")

        embed.set_thumbnail(url=url2)
        await ctx.message.delete()
        await ctx.send("@everyone")
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title=f"{activity} \\o/", description=f"{descr}")
        embed.add_field(name="Date:", value=date)
        embed.add_field(name="Time:", value=time)
        await ctx.message.delete()
        await ctx.send("@everyone")
        await ctx.send(embed=embed)


# command sections for incoming members to get rules and such

# command section for UWU bot
discord_token = utils.read_discord_token()
bot.run(discord_token)
