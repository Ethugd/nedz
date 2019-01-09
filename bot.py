import discord
from discord.ext import commands
import random
import math
from utils import MyToken

description = 'Custom multi-purpose bot for Classic WoW Oceania.'
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
<<<<<<< HEAD
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
    
    
=======
    role = None
    if not payload.guild_id: 
        return
    if payload.message_id == 523093753242714113:
        if payload.emoji.id == 523088959312625684: 
            role = discord.Object(506818004273725450) 
        elif payload.emoji.id == 523089719291281408:
            role = discord.Object(506818248168177674) 
    elif payload.message_id == 523093774679801857:
        if payload.emoji.id == 523077042883919875: 
            role = discord.Object(522827107785506816) 
        elif payload.emoji.id == 523077059480649738:
            role = discord.Object(522827110340100096)
        elif payload.emoji.id == 523077066946641921: 
            role = discord.Object(522827112609087500) 
        elif payload.emoji.id == 523077079424827395:
            role = discord.Object(522827115645894657)
        elif payload.emoji.id == 523077092657725444: 
            role = discord.Object(522827118217003009) 
        elif payload.emoji.id == 523077105018339338:
            role = discord.Object(522827120896901123)
        elif payload.emoji.id == 523077113851543554: 
            role = discord.Object(522827123694764042) 
        elif payload.emoji.id == 523077126229065728:
            role = discord.Object(522827126693560320)
        elif payload.emoji.id == 523077137075404801: 
            role = discord.Object(522827129352617984)     
    if role:
        guild = bot.get_guild(payload.guild_id) 
        member = guild.get_member(payload.user_id)         
        await member.add_roles(role, reason='Reaction role') 

>>>>>>> 429f11eae2f6265eebbee4b2ec7ea1203b51e2f3
@bot.event
async def on_raw_reaction_remove(payload): #
    role = None
    if not payload.guild_id: 
        return
    if payload.message_id == 523093753242714113:
        if payload.emoji.id == 523088959312625684: 
            role = discord.Object(506818004273725450) 
        elif payload.emoji.id == 523089719291281408:
            role = discord.Object(506818248168177674) 
    elif payload.message_id == 523093774679801857:
        if payload.emoji.id == 523077042883919875: 
            role = discord.Object(522827107785506816) 
        elif payload.emoji.id == 523077059480649738:
            role = discord.Object(522827110340100096)
        elif payload.emoji.id == 523077066946641921: 
            role = discord.Object(522827112609087500) 
        elif payload.emoji.id == 523077079424827395:
            role = discord.Object(522827115645894657)
        elif payload.emoji.id == 523077092657725444: 
            role = discord.Object(522827118217003009) 
        elif payload.emoji.id == 523077105018339338:
            role = discord.Object(522827120896901123)
        elif payload.emoji.id == 523077113851543554: 
            role = discord.Object(522827123694764042) 
        elif payload.emoji.id == 523077126229065728:
            role = discord.Object(522827126693560320)
        elif payload.emoji.id == 523077137075404801: 
            role = discord.Object(522827129352617984) 
    if role:
        guild = bot.get_guild(payload.guild_id) 
        member = guild.get_member(payload.user_id)         
        await member.remove_roles(role, reason='Reaction role')

bot.run(MyToken.TOKEN) #bot token
