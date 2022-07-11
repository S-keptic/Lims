import discord
from discord.ext import commands
import random
import requests
import os
from os import environ, link
import askitsu
kitsu = askitsu.Client()
 


client=commands.Bot(command_prefix="!", intents=discord.Intents.all())

#onchangingpresance
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name="!help"))

#OnmentioningClient

@client.event
async def on_message(message):
    if client.user.mention in message.content.split():
       await message.reply("**Type !help for more commmands**")
    await client.process_commands(message)



@client.command()
async def ping(ctx):
    await ctx.reply(f"`Pong 🏓 {round(client.latency* 1000)}ms`")



client.remove_command("help")

#help

@client.command()
async def help(ctx):
    em=discord.Embed(title="***LIMS HELP MENUE***📙",colour=discord.Colour.red(),description="`My prefix is !`")
    em.add_field(name="__1)Utility command 🤖 __",value="```!anime <anime name>\n!manga <manga name>\n!stats```")
    em.add_field(name="__2)SFW commands 🤖 __",value="```!hug !pat !cuddle !slap !punch !avatar !neko !tickle !wallpaper !cry !smug ```",inline=False)
    em.add_field(name="__3)NSFW commands 🤖 __",value="```!fuck !bj !boobs !spank```",inline=False)
    em.set_image(url="https://cdn.discordapp.com/attachments/994580760113717258/994912666483175474/standard2.gif")
    em.set_footer(text="Lims Bot🌸",icon_url="https://cdn.discordapp.com/attachments/994580760113717258/994913278042054776/botpfp1.jpeg")
    await ctx.reply(embed=em)








#utility functions


#stats of bot
@client.command()
async def stats(ctx):
    em=discord.Embed(title="***Lims Stats***",color=(discord.Color.purple()),description=" ")
    em.add_field(name="`Server Count`",value=f"{len(client.guilds)}",inline=True)
    em.add_field(name="`Heartbeat`",value=f"{round(client.latency*1000)} ms",inline=True)

    em.set_footer(text="Lims Bot🌸 ",icon_url="https://cdn.discordapp.com/attachments/994580760113717258/994913278042054776/botpfp1.jpeg")
    await ctx.reply(embed=em)

#animesearch

@client.command(name="anime")
async def anime(ctx, *, query: str) -> None:
    query_formatted = query.replace(" ", "+")
    kitsu = askitsu.Client()

    anime = await kitsu.search_anime(query_formatted, limit=1)
    em=discord.Embed(title="***Anime Search***",colour=(discord.Colour.purple()),description=
    f"***Anime***: {anime.title.en}    \n\n***Episodes***: {anime.episode_count}    \n\n***Description***: {anime.synopsis}  ")

    em.set_image(url=f"{anime.poster_image.small}")
    em.add_field(name="`Started at`",value=f"{anime.started_at}",inline=True)
    em.add_field(name="`Ended at`",value=f"{anime.ended_at}",inline=True)
    em.add_field(name="`Status`",value=f"{anime.status}",inline=True)
    em.add_field(name="`Score`",value=f"{anime.rating}",inline=True)
    em.add_field(name="`Age rating`",value=f"{anime.age_rating}",inline=True)
    em.add_field(name="`NSFW`",value=f"{anime.nsfw}",inline=True)




    await kitsu.close()
    await ctx.reply(embed=em)


#mangasearch

@client.command(name="manga")
async def manga(ctx, *, query: str) -> None:
    query_formatted = query.replace(" ", "+")
    kitsu = askitsu.Client()

    manga = await kitsu.search_manga(query_formatted, limit=1)
    em=discord.Embed(title="***Manga Search***",colour=(discord.Colour.purple()),description=
    f"***Manga***: {manga.title.en}    \n\n***Chapters***: {manga.chapter_count}    \n\n***Description***: {manga.synopsis}  ")

    em.set_image(url=f"{manga.poster_image.small}")
    em.add_field(name="`Started at`",value=f"{manga.started_at}",inline=True)
    em.add_field(name="`Ended at`",value=f"{manga.ended_at}",inline=True)
    em.add_field(name="`Status`",value=f"{manga.status}",inline=True)
    em.add_field(name="`Age rating`",value=f"{manga.age_rating}",inline=True)
    em.add_field(name="`Rank`",value=f"{manga.rating_rank}",inline=True)
    em.add_field(name="`Score`",value=f"{manga.rating}",inline=True)

    await kitsu.close()
    await ctx.reply(embed=em)














#safeforwatching[sfw]

#hug

@client.command()
async def hug(ctx,user:discord.Member=None):
    if user is None:
        await ctx.reply("**Mention Someone to hug!!**")
    else:
        r= requests.get("https://nekos.life/api/v2/img/hug")
        res=r.json()
        em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention} ***hugs*** {user.mention}")
        em.set_image(url=res['url'])
        await ctx.reply(embed=em)

#pat
@client.command()
async def pat(ctx,user:discord.Member=None):
    if user is None:
        await ctx.reply("**Mention someone to pat!!**")
    
    else:

        r= requests.get("https://nekos.life/api/v2/img/pat")
        res=r.json()
        em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention} ***pats*** {user.mention}")
        em.set_image(url=res['url'])
        await ctx.reply(embed=em)

#neko


@client.command()
async def neko(ctx):
    r= requests.get("https://nekos.life/api/v2/img/neko")
    res=r.json()
    em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention}")
    em.set_image(url=res['url'])
    await ctx.reply(embed=em)

#kitsune


@client.command()
async def kitsune(ctx):
    r= requests.get("https://neko-love.xyz/api/v1/kitsune")
    res=r.json()
    em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention}")
    em.set_image(url=res['url'])
    await ctx.reply(embed=em)




#cry


@client.command()
async def cry(ctx):
    r= requests.get("https://neko-love.xyz/api/v1/cry")
    res=r.json()
    em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention}")
    em.set_image(url=res['url'])
    await ctx.reply(embed=em)



#slap


@client.command()
async def slap(ctx,user:discord.Member=None):
    if user is None:
        await ctx.reply("**Mention someone to slap!!**")
    else:
        r= requests.get("https://nekos.life/api/v2/img/slap")
        res=r.json()
        em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention} ***slaps*** {user.mention}")
        em.set_image(url=res['url'])
        await ctx.reply(embed=em)

#smug


@client.command()
async def smug(ctx):
    r= requests.get("https://nekos.life/api/v2/img/smug")
    res=r.json()
    em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention}")
    em.set_image(url=res['url'])
    await ctx.reply(embed=em)

#punch


@client.command()
async def punch(ctx,user:discord.Member=None):
    if user is None:
        await ctx.reply("**Mention someone to punch!!**")
    else:
        r= requests.get("https://neko-love.xyz/api/v1/punch")
        res=r.json()
        em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention} ***punches*** {user.mention}")
        em.set_image(url=res['url'])
        await ctx.reply(embed=em)

#waifu
@client.command()
async def waifu(ctx):
    r= requests.get("https://nekos.life/api/v2/img/waifu")
    res=r.json()
    em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention}")
    em.set_image(url=res['url'])
    await ctx.reply(embed=em)



#gasm
@client.command()
async def gasm(ctx):
    r= requests.get("https://nekos.life/api/v2/img/gasm")
    res=r.json()
    em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention}")
    em.set_image(url=res['url'])
    await ctx.reply(embed=em)

#cuddle
@client.command()
async def cuddle(ctx,user:discord.Member=None):
    if user is None:
        await ctx.reply("**Mention someone to cuddle!!**")
    else:    
        r= requests.get("https://nekos.life/api/v2/img/cuddle")
        res=r.json()
        em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention} ***cuddles*** {user.mention}")
        em.set_image(url=res['url'])
        await ctx.reply(embed=em)

#feed
@client.command()
async def feed(ctx,user:discord.Member=None):
    if user is None:
        await ctx.reply("**Mention someone to feed!!**")
    else:
        r= requests.get("https://nekos.life/api/v2/img/feed")
        res=r.json()
        em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention} ***feeds*** {user.mention}")
        em.set_image(url=res['url'])
        await ctx.reply(embed=em)

#avatar
@client.command()
async def avatar(ctx):
    r= requests.get("https://nekos.life/api/v2/img/avatar")
    res=r.json()
    em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention}")
    em.set_image(url=res['url'])
    await ctx.reply(embed=em)

#meow
@client.command()
async def meow(ctx):
    r= requests.get("https://nekos.life/api/v2/img/meow")
    res=r.json()
    em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention}")
    em.set_image(url=res['url'])
    await ctx.reply(embed=em)

    
#wallpaper
@client.command()
async def wallpaper(ctx):
    r= requests.get("https://nekos.life/api/v2/img/wallpaper")
    res=r.json()
    em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention}")
    em.set_image(url=res['url'])
    await ctx.reply(embed=em)

#tickle
@client.command()
async def tickle(ctx,user:discord.Member=None):
    if user is None:
        await ctx.reply("**Mention someone to tickle!!**")
    else:   
        r= requests.get("https://nekos.life/api/v2/img/tickle")
        res=r.json()
        em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention} ***tickles*** {user.mention}")
        em.set_image(url=res['url'])
        await ctx.reply(embed=em)
#kiss
#kiss
@client.command()
async def kiss(ctx,user:discord.Member=None):
        if user is None:
            await ctx.reply("**Mention someone to kiss!!**")
        else:
            r= requests.get("https://nekos.life/api/v2/img/kiss")
            res=r.json()
            em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention} ***kisses*** {user.mention}")
            em.set_image(url=res['url'])
            await ctx.reply(embed=em)


#ngif

@client.command()
async def ngif(ctx):
    r= requests.get("https://nekos.life/api/v2/img/ngif")
    res=r.json()
    em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention}")
    em.set_image(url=res['url'])
    await ctx.reply(embed=em)



#nsfw[not safe for work]


#bj




blowjob=['https://cdn.discordapp.com/attachments/993792792360915035/993792859876630589/1.gif',
    'https://cdn.discordapp.com/attachments/993792792360915035/993795470461771786/2.gif',
    "https://cdn.discordapp.com/attachments/993792792360915035/993966283202756608/3.gif",
    "https://cdn.discordapp.com/attachments/993792792360915035/993966283567673404/4.gif",
    "https://cdn.discordapp.com/attachments/993792792360915035/993966284196814938/5.gif",
    "https://cdn.discordapp.com/attachments/993792792360915035/993966285002125432/7.gif",
    "https://cdn.discordapp.com/attachments/993792792360915035/993966285350244352/8.jpg",
    "https://cdn.discordapp.com/attachments/993792792360915035/993966285606113401/9.gif",
    "https://cdn.discordapp.com/attachments/993792792360915035/993966285991981067/10.gif",
    "https://cdn.discordapp.com/attachments/993792792360915035/993966286306545684/11.gif",
    "https://cdn.discordapp.com/attachments/993792792360915035/993966286583386112/12.gif",
    "https://cdn.discordapp.com/attachments/993792792360915035/993971957500498052/14.gif",
    "https://cdn.discordapp.com/attachments/993792792360915035/993971957815054356/15.gif",
    "https://cdn.discordapp.com/attachments/993980711931490374/994554034981712012/11.gif",
    "https://cdn.discordapp.com/attachments/993980711931490374/994554035547951134/16.gif",
    "https://cdn.discordapp.com/attachments/993980711931490374/994554036286144522/17.gif",

    ]


    
@client.command()
async def bj(ctx):
    if ctx.channel.is_nsfw():
        embed=discord.Embed(colour=(discord.Colour.random()),
        description=f"{ctx.author.mention}")
        embed.set_image(url=(random.choice(blowjob)))
        await ctx.reply(embed=embed)
    else:
        await ctx.reply("***This is not a NSFW channel 🚫 , Please enable NSFW in your channel settings***")

#fuck
fucc=[
    "https://cdn.discordapp.com/attachments/993980713173012520/993980827585224784/2.gif",
    "https://cdn.discordapp.com/attachments/993980711931490374/993987842642554910/ezgif.com-gif-maker.gif",
    "https://cdn.discordapp.com/attachments/993980713173012520/993987055824683048/4.gif",
    "https://cdn.discordapp.com/attachments/993980711931490374/993988445871538247/ezgif.com-gif-maker1.gif",
    "https://cdn.discordapp.com/attachments/993980713173012520/993987057196216371/6.gif",
    "https://cdn.discordapp.com/attachments/993980713173012520/993987058001526924/7.gif",
    "https://cdn.discordapp.com/attachments/993980713173012520/993987058651648021/8.gif",
    "https://cdn.discordapp.com/attachments/993980713173012520/993987059209482420/9.gif",
    "https://cdn.discordapp.com/attachments/993980713173012520/993987059922518056/10.gif",
    "https://cdn.discordapp.com/attachments/993980711931490374/994575763162542121/25.gif",
    "https://cdn.discordapp.com/attachments/993980711931490374/994575775246336080/12.gif",
    "https://cdn.discordapp.com/attachments/993980711931490374/994575775917428776/14.gif",
    "https://cdn.discordapp.com/attachments/994578029781188738/994578150891724830/11.gif",
    "https://cdn.discordapp.com/attachments/939199144545878117/994578566719217684/10.gif",
    "https://cdn.discordapp.com/attachments/939199144545878117/994578567281262692/9.gif",
    "https://cdn.discordapp.com/attachments/939199144545878117/994578567675510854/8.gif",
    "https://cdn.discordapp.com/attachments/939199144545878117/994578568183038042/7.gif",
    "https://cdn.discordapp.com/attachments/939199144545878117/994578568501796874/6.gif",
    "https://cdn.discordapp.com/attachments/939199144545878117/994578568925425704/5.gif",
    "https://cdn.discordapp.com/attachments/939199144545878117/994578569378402384/4.gif"
    ]
@client.command()
async def fuck(ctx):
    if ctx.channel.is_nsfw():
        embed=discord.Embed(colour=(discord.Colour.random()),
        description=f"{ctx.author.mention}")
        embed.set_image(url=(random.choice(fucc)))
        await ctx.reply(embed=embed)
    else:
        await ctx.reply("***This is not a NSFW channel 🚫 , Please enable NSFW in your channel settings***")


#spank

@client.command()

async def spank(ctx):
    if ctx.channel.is_nsfw():
        r= requests.get("https://nekos.life/api/v2/img/spank")
        res=r.json()
        em=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention}")
        em.set_image(url=res['url'])
        await ctx.reply(embed=em)
    else:
        await ctx.reply("***This is not a NSFW channel 🚫 , Please enable NSFW in your channel settings***")

    

                    
#boobs
booba=["https://cdn.discordapp.com/attachments/994927245091156008/994927981736755200/1.gif",
        "https://cdn.discordapp.com/attachments/994948123468243055/994948279353737227/2.gif",
        "https://cdn.discordapp.com/attachments/994948123468243055/994948328624238592/1.gif",
        "https://cdn.discordapp.com/attachments/994948123468243055/994948597823053864/3.gif",
        "https://cdn.discordapp.com/attachments/994948123468243055/994948882092015656/5.gif",
        "https://cdn.discordapp.com/attachments/994948123468243055/994949055203512400/4.gif",
        "https://cdn.discordapp.com/attachments/994948123468243055/994949380006215753/7.gif",
        "https://cdn.discordapp.com/attachments/994948123468243055/994950339063185429/8.gif"]


@client.command()
async def boobs(ctx):
    if ctx.channel.is_nsfw():
        embed=discord.Embed(colour=(discord.Colour.random()),description=f"{ctx.author.mention}")
        embed.set_image(url=(random.choice(booba)))
        await ctx.reply(embed=embed)
 




client.run("OTkzMDg4MzMzNjM2OTYwMjY2.G3snmx.BTsi0b7BL0UtmxlsEczsDcV3Enew9LQ8Yk2ODo")
