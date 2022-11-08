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

def special_number():
    number=random.randint(0,99)
    return number