import discord
from discord.ext import commands
import random
import math
from utils import MyToken

description = 'Custom multi-purpose bot for Classic WoW Oceania.'

bot = commands.Bot(command_prefix='??', description=description)
bot.remove_command("help")
WOW_OCE = 378811843445129217

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_member_join(member):
    if member.guild.id = WOW_OCE:
        channel = bot.get_channel(378811843445129219)
        channel2 = bot.get_channel(379611647469158400)

        welcomeMsg = [f"Welcome to **Classic WoW Oceania!**", 
                      f"G'day mate, enjoy your stay!", 
                      f"Hey mate, thanks for joining!", 
                      f"Crikey! A new member has appeared.", 
                      ]
    
        embed=discord.Embed(colour=0xf6d139)#title=f"{random.choice(welcomeMsg)}", description="Check out #rules-and-info to get started.")
        embed.add_field(name=f"{random.choice(welcomeMsg)}", value=f"Please check out {channel2.mention}")
        embed.set_author(name=f"{member}", icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)

        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])

        embed.set_footer(icon_url=member.guild.icon_url, text=f"You are the {ordinal(member.guild.member_count)} member!")
        await channel.send(embed=embed)

@bot.event
async def on_raw_reaction_add(payload): #
    if not payload.guild_id: 
        return
		
    if payload.message_id == 506826293719990272:

		if payload.emoji.id == 522768968247803924: 
			role = discord.Object(506818004273725450) 
		elif payload.emoji.id == 522768858369753138:
			role = discord.Object(506818248168177674)
		elif payload.emoji.id == 522771058454167552:
			role = discord.Object(506827520625082389)
		else:
			pass
			
    elif payload.message_id == 506826293719990272:

		if payload.emoji.id == 522768968247803924: 
			role = discord.Object(506818004273725450) 
		elif payload.emoji.id == 522768858369753138:
			role = discord.Object(506818248168177674)
		elif payload.emoji.id == 522771058454167552:
			role = discord.Object(506827520625082389)
		else:
			pass
			
	else:
		pass
		
    guild = bot.get_guild(payload.guild_id) 
    member = guild.get_member(payload.user_id) 		


    await member.add_roles(role, reason='Reaction role') 
    
    
@bot.event
async def on_raw_reaction_remove(payload): #Same shit but it's the other way around, checking when a reaction is removed and then removing the role
    if not payload.guild_id:
        return
        
    if payload.message_id != 506826293719990272:
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

bot.run(MyToken.TOKEN) #bot token
