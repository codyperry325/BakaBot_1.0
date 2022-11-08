@bot.command()
async def uwufy(ctx):
    message = await ctx.channel.fetch_message(ctx.message.reference.message_id)


#try and get the tagged message instead of just doing the last message ;)