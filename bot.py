import discord
from discord.ext import commands
import random
import math
import token

description = 'Custom multi-purpose bot for Classic WoW Oceania.'

bot = commands.Bot(command_prefix='??', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(378811843445129219)
    channel2 = bot.get_channel(379611647469158400)

    welcomeMsg = [f"Welcome to **Classic WoW Oceania!**", 
                  f"G'day **{member.name}**, enjoy your stay!"
                  f"Hey **{member.name}**, thanks for joining!",
                  f"Crikey! A wild **{member.name}** has appeared.",
                  ]
    
    embed=discord.Embed(colour=0xf6d139)#title=f"{random.choice(welcomeMsg)}", description="Check out #rules-and-info to get started.")
    embed.add_field(name=f"{random.choice(welcomeMsg)}", value=f"Check out {channel2.mention}")
    embed.set_author(name=f"{member}", icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)

    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])

    embed.set_footer(icon_url=member.guild.icon_url, text=f"You are the {ordinal(member.guild.member_count)} member!")
    await channel.send(embed=embed)

@bot.event
async def on_raw_reaction_add(payload): #Event fires when an emoji is added to a message regardless of it being in the bot's cache
    if not payload.guild_id: #Checking to see if the reaction was added in a server or dms
        return
        
    if payload.message_id != 506826280055078913: #Checking the message id is the same to the one we want
        return

    guild = bot.get_guild(payload.guild_id)  #Getting a guild object with the id the payload gives us
    member = guild.get_member(payload.user_id) #Get a member object of the person who added the reaction

    if payload.emoji.id == 522768968247803924: #We're checking to see if the reaction added is this. That string is the unicode code point of the check emoji 
        role = discord.Object(506818004273725450) #Getting a role object to add to the person who added the reaction
    elif payload.emoji.id == 522768858369753138:
        role = discord.Object(506818248168177674)
    elif payload.emoji.id == 522771058454167552:
        role = discord.Object(506827520625082389)
    else:
        return # If the emoji added isn't the one we want

    await member.add_roles(role, reason='Reaction role') #Add the role to the person who added the role
    
    
@bot.event
async def on_raw_reaction_remove(payload): #Same shit but it's the other way around, checking when a reaction is removed and then removing the role
    if not payload.guild_id:
        return
        
    if payload.message_id != 506826280055078913:
        return

    guild = bot.get_guild(payload.guild_id) 
    member = guild.get_member(payload.user_id) 

    if payload.emoji.id == 522768968247803924:
        role = discord.Object(506818004273725450)
    elif payload.emoji.id == 522768858369753138:
        role = discord.Object(506818248168177674)
    elif payload.emoji.id == 522771058454167552:
        role = discord.Object(506827520625082389)
    else:
        return

    await member.remove_roles(role, reason='Reaction role')

bot.run(token.TOKEN) #bot token