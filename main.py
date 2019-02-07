import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import requests
import json
import praw
import aiohttp
from imgurpython import ImgurClient
from random import choice, shuffle

Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = commands.Bot(description="MultiVerse Official Bot", command_prefix=commands.when_mentioned_or("mv!" ), pm_help = True)
reddit = praw.Reddit(client_id='G-SK66FZT8at9g',
                     client_secret='DLqIkkdoD0K8xKpxuaMAhRscrS0',
                     user_agent='android:com.G-SK66FZT8at9g.SolarBot:v1.2.3 (by /u/LaidDownRepaer)')

CLIENT_ID = "1fd3ef04daf8cab"
CLIENT_SECRET = "f963e574e8e3c17993c933af4f0522e1dc01e230"
imgur = ImgurClient(CLIENT_ID,CLIENT_SECRET)

GIPHY_API_KEY = "dc6zaTOxFJmzC"


client.remove_command('help')


async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='mv!help', type=2))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name=str(len(set(client.get_all_members())))+' users', type=3))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name=str(len(client.servers))+' servers', type=3))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='music'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='I need some upvotes to grow ;('))
        await asyncio.sleep(5)

left = '⏪'
right = '⏩'
r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
general1=discord.Embed(title="General Commands | Page 1", description="**__mv!donate__** \nSends donation link \n\n**__mv!invite__** or **__mv!authlink__** \nUse it to invite our bot to your server \n\n**__mv!upvote__**\nUse this command to upvote our bot(Link will be in dm)\n\n **__mv!google__**\n Use it like- ``mv!google <anything>`` to google anything\n\n**__mv!youtube__**\nUse it like- ``mv!youtube <anything>`` to search anything on youtube\n\n**__mv!membernames__**\nUse it to get member names in dm\n\n**__mv!invites__** \nUse it like ``mv!invites @user`` or ``mv!invite`` for get invites done by you/tagged person in server. \n__Note:__**If bot does not responds that means you do not have invited any member on that server.**\n\n**__mv!remind__**\nUse it like ``mv!remind <time in minutes> <text like what to remind>`` Example: ``mv!remind 2 Drink water``.\n\n**__mv!helpmusic__**\nTo get list of music commands like: mv!play,mv!skip,etc.", color = discord.Color((r << 16) + (g << 8) + b))
general2=discord.Embed(title="General Commands | Page 2", description="**__mv!serverinvite__** \nUse it to get server invite link.\n\n**__mv!avatar__**\nUse it like ``mv!avatar or mv!avatar @user``\n\n**__mv!ping__**\nUse it to check ping of bot\n\n**__mv!enterme__**\nUse it like ``mv!enterme <giveaway channel>`` to enter in a giveaway running in a particular channel\n\n**__mv!poll__**\nUse it like ``mv!poll Question Option1 Option2 ..... Option9``.\n\n**__mv!github__**\nUse it like- ``mv!github uksoftworld``\n\n**__mv!bottutorial__**\nUse it like ``mv!bottutorial <tutorial name by darklegend>``\n\n**__mv!dyno__**\nUse it like ``mv!dyno <dyno command name>``\n\n**__mv!happybirthday @user__**\nTo wish someone happy birthday\n\n**__mv!verify__**Use it to get verified role. Note- It needs proper setup.\n\n**__mv!rank__**\nUse it to check your daily multiverse rank(xp + level)\n\n**__mv!afk <anything>__**\nTo set afk\n\n**__mv!write note <anything>__**\nTo write note and save it", color = discord.Color((r << 16) + (g << 8) + b))
general3=discord.Embed(title="Fun Commands <==> General Commands | Page 3", description="**__mv!joke__**\n\n**__mv!kiss @user__**\n\n**__mv!hug @user__**\n\n**__mv!slap @user__**\n\n**__mv!damn__**\n\n**__mv!burned__**\n\n**__mv!savage__**\n\n**__mv!thuglife__**\n\n**__mv!membernames__**\n\n**__mv!gender @user__**\n\n**__mv!virgin @user__**\n\n**__mv!meme__**\n\n**__mv!rolldice__**\n\n**__mv!flipcoin__**\n\n**__mv!guess__**\n\n**__mv!movie <movie name>__**\n\n**__mv!rps <rock ,paper or scissors>__**\n\n**__mv!urban <string>__**\n\n**__mv!imgursearch <anything>__**\n\n**__mv!gifsearch <anything>__**\n\n**__mv!talk anything__**\nUse it to make bot say anything in voice channel", color = discord.Color((r << 16) + (g << 8) + b))
general4=discord.Embed(title="Economy Commands <==> General Commands | Page 4", description="**__mv!daily__**\n\n**__mv!bal @user or mv!bal__**\n\n**__mv!transfer @user <amount>__**\n\n**__mv!lb__**\n\n**__mv!coinflip <heads or tails> <amount>__**\n\n**__mv!dice <1-6 dice number> <amount>__**\n\n**__mv!work__**", color = discord.Color((r << 16) + (g << 8) + b))
mod1=discord.Embed(title="Admin and Mod Commands | Page 1", description="**__mv!partner(Admin permission required) (Cooldown of 12hours)__** \nUse it like ``mv!partner <partnership description>`` to partner with many servers with are connected with MultiVerse Official bot \n\n**__mv!dm(Admin permission required)__** \nUse it like ``mv!dm @user <text>`` to dm user from bot \n\n**__mv!say(Admin permission required)__**\nUse it like ``mv!say <text>``\n\n **__mv!showme(Requires a role named Giveaways)__**\n To see how many people are taking part in giveaway\n\n**__mv!pickwinner(Requires a role named Giveaways)__**\nTo pick winner of currentmost giveaways\n\n**__mv!embed(Admin permission required__**\nUse it like ``mv!embed <text>``\n\n**__mv!membercount(Kick members Permission Required)__** \n Use it to get membercount of server\n\n**__mv!lock(Kick members Permission Required)__**\nUse it like ``mv!lock #channel or mv!lock`` to lock a channel\n\n**__mv!unlock(Kick members Permission Required)__**\nUse it like ``mv!unlock #channel or mv!unlock`` to unlock a channel", color = discord.Color((r << 16) + (g << 8) + b))
mod2=discord.Embed(title="Admin and Mod Commands | Page 2", description="**__mv!removemod(Admin Permission Required)__** \nUse it like ``mv!removemod @user`` to remove him from mod. Note-You need Moderator role in your server below bot to use it.\n\n**__mv!makemod(Admin Permission Required)__**\nUse it like ``mv!makemod @user`` to make him mod. Note-You need Moderator role in your server below multiverse bot to use it.\n\n**__mv!friend(Admin Permission Required)__**\nUse it like ``mv!friend @user`` to give anyone Friend of Owner role\n\n**__mv!role(Manage Roles Permission Required)__**\nUse it like ``mv!role @user/all <rolename>`` to give/take role from @user or all in server.\n\n**__mv!setnick(Manage nickname permission required)__**\nUse it like ``mv!setnick all/@user <New nickname>`` to change the nickname of tagged user or all in the server.\n\n**__mv!english(Kick members Permission Required)__**\nUse it like ``mv!english @user`` when someone speaks languages other than English.\n\n**__mv!serverinfo(Kick members Permission Required)__**\nUse it like ``mv!serverinfo`` to get server info\n\n**__mv!userinfo(Kick members Permission Required)__**\nUse it like ``mv!userinfo @user`` to get some basic info of tagged user.", color = discord.Color((r << 16) + (g << 8) + b))
mod3=discord.Embed(title="Admin and Mod Commands | Page 3", description="**__mv!unbanall(Unban members Permission Required)__** \nUse it like ``mv!unbanall`` to unban all members\n\n**__mv!unban__**\nUse it like: ``mv!unban userid`` to unban user.\n\n**__mv!kick(Kick members Permission Required)__**\nUse it like ``mv!kick @user`` to kick any user\n\n**__mv!muteinchannel(Ban members Permission Required)__**\nUse it like ``mv!muteinchannel @user <time in minutes>`` Example- ``mv!muteinchannel @user 1`` to mute user for 1min.\n\n**__mv!unmuteinchannel(Ban members Permission Required)__**\nUse it like ``mv!unmuteinchannel @user`` to unmute user from that channel.\n\n**__mv!roles(Kick members Permission Required)__**\nUse it to check roles present in server.\n\n**__mv!purge(Manage Messages Permission Required)__**\nUse it like ``mv!purge <number>`` to clear any message.\n\n**__mv!mute(Mute members Permission Required)__**\nUse it like ``mv!mute @user <time in minutes>`` to mute any user. **Note-You need to add Muted role in your server if it is not already there also you must need to change permission of all channels and disable send_message permission for that role.**\n\n**__mv!unmute(Mute members Permission Required)__**\nUse it like ``mv!unmute @user`` to unmute anyone.", color = discord.Color((r << 16) + (g << 8) + b))
mod4=discord.Embed(title="Admin and Mod Commands | Page 4", description="**__mv!ban(Ban members Permission Required)__** \nUse it like ``mv!ban @user`` to ban any user\n\n**__mv!rules(Kick members Permission Required)__**\nUse it like ``mv!rules @user <violation type>`` to warn user\n\n**__mv!warn(Kick members Permission Required)__**\nUse it like ``mv!warn @user <violation type>`` to warn any user.\n\n**__mv!norole(Kick members Permission Required)__**\nUse it like ``mv!norole @user`` to warn anyone if he/she asks for promotion.\n\n**__mv!getuser(Kick members Permission Required)__**\nUse it like ``mv!getuser rolename`` to get list of all users having a that role.\n\n**__mv!roleinfo(Manage roles Permission Required)__**\nUse it like ``mv!roleinfo <rolename>`` to get basic info about that role.\n\n**__mv!addchannel(Administrator Permission Required)__**\nUse it like ``mv!addchannel <channelname>`` to add that channel in server.\n\n**__mv!delchannel(Administrator Permission Required)__**\nUse it like ``mv!delchannel <channelname>`` to delete that channel in server.\n\n**__mv!resetnick__**\nUse it like: ``mv!resetnick @user/all`` to reset nickname of @user or all in the server", color = discord.Color((r << 16) + (g << 8) + b))

gen_cmd = (general1, general2, general3, general4)
mod_cmd = (mod1, mod2, mod3, mod4)

def predicate(message, l, r):
    def check(reaction, user):
        if reaction.message.id != message.id or user == client.user:
            return False
        if l and reaction.emoji == left:
            return True
        if r and reaction.emoji == right:
            return True
        return False

    return check



@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started Our BOT')
    print('Created by Utkarsh')
    client.loop.create_task(status_task())
    
def is_dark(ctx):
    return ctx.message.author.id == "420525168381657090"

def is_staff(ctx):
    return ctx.message.author.id in ["420525168381657090", "514856260353392660", "472680171451973632" ,"442575516684386304" ,"425676648818671618", "399274658027012098", "437525938582847489"]

def is_shreyas(ctx):
    return ctx.message.author.id == "376602841625919488"

@client.event
async def on_message(message):
    await client.process_commands(message)
    channel = client.get_channel('518710986799316992')
    if message.server is None and message.author != client.user:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed=discord.Embed(title=f"{message.author.name} sent", description=f"{message.content}", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_thumbnail(url= message.author.avatar_url)
        await client.send_message(channel, '{} ID: {}'.format(message.author.name,message.author.id))
        await client.send_message(channel, embed=embed)

@client.event
async def on_reaction_add(reaction, user):
  if reaction.message.server is None:
      if reaction.emoji == '🇬':
          index = 0
          while True:
              msg = await client.send_message(user, embed=gen_cmd[index])
              l = index != 0
              r = index != len(gen_cmd) - 1
              if l:
                  await client.add_reaction(msg, left) 
              if r:
                  await client.add_reaction(msg, right)
              react, user = await client.wait_for_reaction(check=predicate(msg, l, r))
              if react.emoji == left:
                  index -= 1
              elif react.emoji == right:
                  index += 1
              await client.delete_message(msg)
      if reaction.emoji == '🇲':
          index = 0
          while True:
              msg = await client.send_message(user, embed=mod_cmd[index])
              l = index != 0
              r = index != len(mod_cmd) - 1
              if l:
                  await client.add_reaction(msg, left) 
              if r:
                  await client.add_reaction(msg, right)
              react, user = await client.wait_for_reaction(check=predicate(msg, l, r))
              if react.emoji == left:
                  index -= 1
              elif react.emoji == right:
                  index += 1
              await client.delete_message(msg)
    
      if reaction.emoji == '🏵':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Setup Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'Setting up Welcomer log(Admin Permission required) ',value ='Use mv!setupwelcomer. It will add a welcome channel. Just put that channel in your desired category and it will send all logs there.\n\n**__Note:__** **There is an update from which you can setup channel by just tagging that channel.** __Ex:__ ``mv!set-welcome-channel #channel``. **If you wanna remove that channel from setting then use** ``mv!unset-welcome-channel`` **and if you wanna get the welcome channel name then use** ``mv!get-welcome-channel``.',inline = False)
        embed.add_field(name = 'Setting up AutoPartner Channel(Admin Permission required)',value ='Using ``mv!setuppartner`` command create a channel named multiverse-partner and then you can use mv!partner to partner with other servers.',inline = False)
        embed.add_field(name = 'Setting up Giveaway feature(Manage roles permission required) ',value ='Just add a role named ``Giveaways`` and give that role to user who wanna be giveaway manager. Then use ``mv!help`` and check giveaway commands.',inline = False)
        embed.add_field(name = 'Setting up Reaction Verification(Admin Permission required) ',value ='Just add a role named ``Verified`` then remove permission from everyone to send message in all channels. Also add permission of verified role to send message in chatting channels. Then use ``mv!setreactionverify`` it will automatically add a channel and post information about verification. **__Note__** **Sometimes it does not sends message in channel named #verify-for-chatting when this command is used so reuse that command in such case**. Also if it does not works then use ``mv!reactionverify`` command in your verification channel',inline = False)
        embed.add_field(name = 'Setting up Multiverse bot log(Admin Permission required) ',value ='Use ``mv!setuplog`` and it will automatically add a log channel and log all stuffs there.',inline = False)
        react_message = await client.send_message(user,embed=embed)
        await asyncio.sleep(30)
        await client.delete_message(react_message)
      if reaction.emoji == '🎦':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Emoji Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'mv!wow',value ='WOW emoji <a:WOW:515854429485006848>',inline = False)
        embed.add_field(name = 'mv!cat',value ='Cat emoji <a:agooglecat:516174312294842389>',inline = False)
        embed.add_field(name = 'mv!surprised',value ='Surprised emoji <a:eyebigger:516174315058626560>',inline = False)
        embed.add_field(name = 'mv!angry',value ='Angry emoji <a:angear:516174316950388772>',inline = False)
        embed.add_field(name = 'mv!fearfromme',value ='Scary emoji <a:shiroeglassespush:516174320532193289>',inline = False)
        embed.add_field(name = 'mv!dank',value ='DankMemer emoji <a:OnThaCoco:515853700682743809>',inline = False)
        embed.add_field(name = 'mv!thinking1',value ='Think emoji1 <a:thinking:516183328613990400>',inline = False)
        embed.add_field(name = 'mv!thinking2',value ='Think emoji2 <a:thinking2:516183323127709699>',inline = False)
        embed.add_field(name = 'mv!happy',value ='Happy emoji <a:happy:516183323052212236>',inline = False)
        embed.add_field(name = 'mv!santa',value ='Santa emoji <a:santa:517232271678504970>',inline = False)
        embed.add_field(name = 'mv!lol',value ='LoL emoji <a:lol:517232283670020096>',inline = False)
        embed.add_field(name = 'mv!love',value ='Love emoji <a:love:517232300912672774>',inline = False)
        embed.add_field(name = 'mv!mad',value ='Mad emoji <a:mad:517232301176913951>',inline = False)
        embed.add_field(name = 'mv!alien',value ='Alien emoji <a:alien:517232332663422986>',inline = False)
        embed.add_field(name = 'mv!hi',value ='Saying Hi emoji <a:hi:517232279148429313>',inline = False)
        react_message = await client.send_message(user,embed=embed)
        await asyncio.sleep(30)
        await client.delete_message(react_message)
  else:
      if reaction.emoji == '🇻':
            role = discord.utils.get(user.server.roles, name='Verified')
            await client.add_roles(user, role)
	
@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == '★彡-welcome-彡★':
            embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check rules and never try to break any one of them', color = 0x36393E)
            embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
            embed.set_thumbnail(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif') 
            embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
            embed.add_field(name='Time of joining', value=member.joined_at)
            await asyncio.sleep(0.4)
            await client.send_message(channel, embed=embed) 
            
@client.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == '★彡-welcome-彡★':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'{member.name} just left {member.server.name}', description='Bye bye 👋! We will miss you 😢', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__User left__', value='**Hope you will be back soon 😕.**', inline=True)
            embed.add_field(name='Your join position was', value=member.joined_at)
            embed.set_thumbnail(url=member.avatar_url)
            await client.send_message(channel, embed=embed)

@client.command(pass_context=True)
async def merrychristmas(ctx, user:discord.Member=None):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    if user is None:
        embed=discord.Embed(title='Merry Christmas', description=f'I wanna wish {ctx.message.author} Merry Christmas {ctx.message.author}', color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/486489391083159574/526968559994404874/gif-153062737.gif')
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title='Merry Christmas', description=f'I wanna wish {user} Merry Christmas {user}', color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/486489391083159574/526968559994404874/gif-153062737.gif')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def imgursearch(ctx, *, term: str=None):
    task = functools.partial(imgur.gallery_search, term,
                             advanced=None, sort='time',
                             window='all', page=0)
    task = client.loop.run_in_executor(None, task)
    try:
        results = await asyncio.wait_for(task, timeout=10)
    except asyncio.TimeoutError:
        await client.say("Error: request timed out")
    else:
        if results:
            shuffle(results)
            msg = "Search results...\n"
            for r in results[:3]:
                msg += r.gifv if hasattr(r, "gifv") else r.link
                msg += "\n"
            await client.say(msg)
        else:
            await client.say("Your search terms gave no results.")

@client.command(pass_context=True)
async def gifsearch(ctx, *keywords):
    if keywords:
        keywords = "+".join(keywords)
    else:
        await client.say('Invalid args')
        return
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title='Search Results for', description=f'{keywords}', color = discord.Color((r << 16) + (g << 8) + b))
    url = ("http://api.giphy.com/v1/gifs/search?&api_key={}&q={}"
           "".format(GIPHY_API_KEY, keywords))
    async with aiohttp.get(url) as r:
        result = await r.json()
        if r.status == 200:
            if result["data"]:
                embed.set_image(url=result["data"][0]["url"])
                embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
                embed.timestamp = datetime.datetime.utcnow()
                await client.say(embed=embed)
            else:
                await client.say("No results found.")
        else:
            await client.say("Error contacting the API")

	
@client.command(pass_context=True)
@commands.check(is_dark)
async def setgame(ctx, *, game:str):
    await client.delete_message(ctx.message)
    await client.change_presence(game=discord.Game(name=game))
    await asyncio.sleep(10)

@client.command(pass_context=True)
async def jointest(ctx):
    member = ctx.message.author
    for channel in member.server.channels:
        if channel.name == '★彡-welcome-彡★':
            embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check rules and never try to break any one of them', color = 0x36393E)
            embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
            embed.set_thumbnail(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif') 
            embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
            embed.add_field(name='Time of joining', value=member.joined_at)
            await asyncio.sleep(0.4)
            await client.send_message(channel, embed=embed) 
	
@client.command(pass_context=True)
async def movie(ctx, *, name:str=None):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        await client.send_typing(ctx.message.channel)
        if name is None:
                embed=discord.Embed(description = "Please specify a movie, *eg. mv!movie Inception*", color = discord.Color((r << 16) + (g << 8) + b))
                x = await client.say(embed=embed)
                await asyncio.sleep(5)
                return await client.delete_message(x)
        key = "4210fd67"
        url = "http://www.omdbapi.com/?t={}&apikey={}".format(name, key)
        response = requests.get(url)
        x = json.loads(response.text)
        embed=discord.Embed(title = "**{}**".format(name).upper(), description = "Here is your movie {}".format(ctx.message.author.name), color = discord.Color((r << 16) + (g << 8) + b))
        if x["Poster"] != "N/A":
            embed.set_thumbnail(url = x["Poster"])
            embed.add_field(name = "__Title__", value = x["Title"])
            embed.add_field(name = "__Released__", value = x["Released"])
            embed.add_field(name = "__Runtime__", value = x["Runtime"])
            embed.add_field(name = "__Genre__", value = x["Genre"])
            embed.add_field(name = "__Director__", value = x["Director"])
            embed.add_field(name = "__Writer__", value = x["Writer"])
            embed.add_field(name = "__Actors__", value = x["Actors"])
            embed.add_field(name = "__Plot__", value = x["Plot"])
            embed.add_field(name = "__Language__", value = x["Language"])
            embed.add_field(name = "__Imdb Rating__", value = x["imdbRating"]+"/10")
            embed.add_field(name = "__Type__", value = x["Type"])
            embed.set_footer(text = "Information from the OMDB API")
            await client.say(embed=embed)
	
@client.command(pass_context=True)
async def tweet(ctx, usernamename:str, *, txt:str):
    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={usernamename}&text={txt}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            embed.title = "{} twitted: {}".format(usernamename, txt)
            await client.say(embed=embed)

@client.command(pass_context=True)
async def ownerinfo(ctx):
    embed = discord.Embed(title="Information about owner", description="Main Creator: DarkLegend", color=0x00ff00)
    embed.set_footer(text="Copyright@UK Soft")
    embed.set_author(name=" Bot Owner Names- DarkLegend#3807: 420525168381657090\nTag<!--Back-->#1488: 399274658027012098")
    embed.add_field(name="Site- https://discordbots.org/bot/515403515217313795", value="Thanks for adding our bot", inline=True)
    await client.say(embed=embed)

	
@client.command(pass_context=True)
async def virus(ctx,user: discord.Member=None,*,hack=None):
    nome = ctx.message.author
    if not hack:
        hack = 'discord'
    else:
        hack = hack.replace(' ','_')
    channel = ctx.message.channel
    x = await client.send_message(channel, '``[▓▓▓                    ] / {}-virus.exe Packing files.``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓                ] - {}-virus.exe Packing files..``'.format(hack))
    await asyncio.sleep(0.3)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {}-virus.exe Packing files...``'.format(hack))
    await asyncio.sleep(1.2)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {}-virus.exe Initializing code.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {}-virus.exe Initializing code..``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {}-virus.exe Finishing.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {}-virus.exe Finishing..``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``Successfully downloaded {}-virus.exe``'.format(hack))
    await asyncio.sleep(2)
    x = await client.edit_message(x,'``Injecting virus.   |``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus..  /``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus... -``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus....\``')
    await client.delete_message(x)
    await client.delete_message(ctx.message)
        
    if user:
        await client.say('`{}-virus.exe` successfully injected into **{}**\'s system.'.format(hack,user.name))
        await client.send_message(user,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
    else:
        await client.say('**{}** has hacked himself ¯\_(ツ)_/¯.'.format(name.name))
        await client.send_message(name,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
	
@client.command(pass_context=True, no_pm=True)
async def urban(ctx, *, msg:str=None):
    await client.send_typing(ctx.message.channel)
    if msg is None:
        await client.say('Use it like: ``mv!urban <string>``')
        return
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        word = ' '.join(msg)
        api = "http://api.urbandictionary.com/v0/define"
        response = requests.get(api, params=[("term", word)]).json()
        if len(response["list"]) == 0:
            return await client.say("Could not find that word!")
        embed = discord.Embed(title = "🔍 Search Word", description = word, color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name = "Top definition:", value = response['list'][0]['definition'])
        embed.add_field(name = "Examples:", value = response['list'][0]["example"])
        embed.set_footer(text = "Tags: " + ', '.join(response['tags']))
        await client.say(embed=embed)
		
@client.command(pass_context=True)
async def rps(ctx, *, message=None):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    await client.send_typing(ctx.message.channel)
    ans = ["rock", "paper", "scissors"]
    pick=ans[random.randint(0, 2)]
    embed=discord.Embed(title = "Bot VS {}".format(ctx.message.author.name), color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
    if message is None:
        await client.say('Use it like ``mv!rps rock or scissors or paper`` anyone of them to make this command work properly')
    if message.lower() != ans[0] and message.lower() != ans[1] and message.lower() != ans[2] :
        return await client.say("Pick Rock Paper or Scissors")
    elif message.lower() == pick:
        embed.add_field(name = "Its a draw!", value = "Bot picked {} too!".format(pick))
        return await client.say(embed=embed)
    else:
        if message.lower()  == "rock" and pick == "paper":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "rock" and pick == "scissors":
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "paper" and pick == "rock":
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "paper" and pick == "scissors":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "scissors" and pick == "rock":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        else:
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)

@client.command(pass_context=True)
async def inviteb(ctx):
    total_uses=0
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    server = ctx.message.channel.server
    invites = await client.invites_from(server)
    invlb = f'Invites of {ctx.message.server.name}\n'
    for invite in invites:
      total_uses += invite.uses
      invlb += f'User: {invite.inviter.name}\nInvites: {invite.uses}\n'
    embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='Invites List',value=invlb)
    embed.add_field(name='Total Invites',value=total_uses)
    embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await client.say(embed=embed)
		
@client.command(pass_context=True)
async def invites(ctx, user:discord.Member=None):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    if ctx.message.server.id == '527430758902661121':
        await client.say('You should use ``mv!checkinvites``')
        return
    if user is None:
        total_uses=0
        embed=discord.Embed(title='__Invites from {}__'.format(ctx.message.author.name), color = discord.Color((r << 16) + (g << 8) + b))
        invites = await client.invites_from(ctx.message.server)
        for invite in invites:
          if invite.inviter == ctx.message.author:
              total_uses += invite.uses
              embed.add_field(name='Invite',value=invite.id)
              embed.add_field(name='Uses',value=invite.uses)
              embed.add_field(name='Channel',value=invite.channel)
              embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.add_field(name='__Total Uses__',value=total_uses)
        await client.say(embed=embed)
    else:
        total_uses=0
        embed=discord.Embed(title='__Invites from {}__'.format(user.name), color = discord.Color((r << 16) + (g << 8) + b))
        invites = await client.invites_from(ctx.message.server)
        for invite in invites:
          if invite.inviter == user:
              total_uses += invite.uses
              embed.add_field(name='Invite',value=invite.id)
              embed.add_field(name='Uses',value=invite.uses)
              embed.add_field(name='Channel',value=invite.channel)
              embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.add_field(name='__Total Uses__',value=total_uses)
        await client.say(embed=embed)
	
@client.command(pass_context=True)
async def checkinvites(ctx, user:discord.Member=None):
    if ctx.message.server.id == '527430758902661121':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        if user is None:
            total_uses=0
            embed=discord.Embed(title='__Invites from {}__'.format(ctx.message.author.name), color = discord.Color((r << 16) + (g << 8) + b))
            invites = await client.invites_from(ctx.message.server)
            for invite in invites:
              if invite.inviter == ctx.message.author:
                  total_uses += invite.uses
                  embed.add_field(name='Invite',value=invite.id)
                  embed.add_field(name='Uses',value=invite.uses)
                  embed.add_field(name='Channel',value=invite.channel)
                  embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.add_field(name='__Total Uses__',value=total_uses)
            await client.say(embed=embed)
            if total_uses >= 20:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter I')
                if role in ctx.message.author.roles:
                    return
                else:
                    await client.add_roles(ctx.message.author, role)
                    await client.say('Congrats! You have got Inviter I role')
            if total_uses >= 30:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter II')
                if role in ctx.message.author.roles:
                    return
                else:
                    await client.add_roles(ctx.message.author, role)
                    await client.say('Congrats! You have got Inviter II role')
            if total_uses >= 50:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter III')
                if role in ctx.message.author.roles:
                    return
                else:
                    await client.add_roles(ctx.message.author, role)
                    await client.say('Congrats! You have got Inviter III role')
            if total_uses >= 80:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter IV')
                if role in ctx.message.author.roles:
                    return
                else:
                    await client.add_roles(ctx.message.author, role)
                    await client.say('Congrats! You have got Inviter IV role')
        else:
            total_uses=0
            embed=discord.Embed(title='__Invites from {}__'.format(user.name), color = discord.Color((r << 16) + (g << 8) + b))
            invites = await client.invites_from(ctx.message.server)
            for invite in invites:
              if invite.inviter == user:
                  total_uses += invite.uses
                  embed.add_field(name='Invite',value=invite.id)
                  embed.add_field(name='Uses',value=invite.uses)
                  embed.add_field(name='Channel',value=invite.channel)
                  embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.add_field(name='__Total Uses__',value=total_uses)
            await client.say(embed=embed)
            if total_uses >= 20:
                role = discord.utils.get(user.server.roles, name='Inviter I')
                if role in user.roles:
                    return
                else:
                    await client.add_roles(user, role)
                    await client.say(f'Congrats! {user.name}, You have got Inviter I role')
            if total_uses >= 30:
                role = discord.utils.get(user.server.roles, name='Inviter II')
                if role in user.roles:
                    return
                else:
                    await client.add_roles(user, role)
                    await client.say(f'Congrats! {user.name} You have got Inviter II role')
            if total_uses >= 50:
                role = discord.utils.get(user.server.roles, name='Inviter III')
                if role in user.roles:
                    return
                else:
                    await client.add_roles(user, role)
                    await client.say(f'Congrats! {user.name} You have got Inviter III role')
            if total_uses >= 80:
                role = discord.utils.get(user.server.roles, name='Inviter IV')
                if role in user.roles:
                    return
                else:
                    await client.add_roles(user, role)
                    await client.say(f'Congrats! {user.name} You have got Inviter IV role')
    else:
        await client.say('You are not allowed to use this command in this server')
        return 

@client.command(pass_context = True)
async def detailedinvites(ctx,*,user:discord.Member=None):
    invite = await client.invites_from(ctx.message.server)
    if user is None:
        for invite in invite:
          if invite.inviter == ctx.message.author:
              r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
              embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
              embed.add_field(name = 'Link used for inviting:',value =f'{invite.url}'.format(), inline=False)
              embed.add_field(name = 'Invites from this link:',value =f'{invite.uses}', inline=False)
              embed.add_field(name = 'Created at:',value =f'{invite.created_at}', inline=False)
              embed.add_field(name = 'Channel:',value =f'{invite.channel}', inline=False)
              embed.add_field(name = 'ID:',value =f'{invite.id}', inline=False)
              await client.say(embed=embed)
    else:
        for invite in invite:
          if invite.inviter == user:
              r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
              embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
              embed.add_field(name = 'Link used for inviting:',value =f'{invite.url}'.format(), inline=False)
              embed.add_field(name = 'Invites from this link:',value =f'{invite.uses}', inline=False)
              embed.add_field(name = 'Created at:',value =f'{invite.created_at}', inline=False)
              embed.add_field(name = 'Channel:',value =f'{invite.channel}', inline=False)
              embed.add_field(name = 'ID:',value =f'{invite.id}', inline=False)
              await client.say(embed=embed)
		
@client.command(pass_context=True)
async def lovedetect(ctx, user: discord.Member = None, *, user2: discord.Member = None):
    shipuser1 = user.name
    shipuser2 = user2.name
    useravatar1 = user.avatar_url
    useravatar2s = user2.avatar_url
    self_length = len(user.name)
    first_length = round(self_length / 2)
    first_half = user.name[0:first_length]
    usr_length = len(user2.name)
    second_length = round(usr_length / 2)
    second_half = user2.name[second_length:]
    finalName = first_half + second_half
    score = random.randint(0, 100)
    filled_progbar = round(score / 100 * 10)
    counter_ = '█' * filled_progbar + '‍ ‍' * (10 - filled_progbar)
    url = f"https://nekobot.xyz/api/imagegen?type=ship&user1={useravatar1}&user2={useravatar2s}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f"{shipuser1} ❤ {shipuser2} Love each others", description=f"Love\n`{counter_}` Score:**{score}% **\nLoveName:**{finalName}**", color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            await client.say(embed=embed)
		
@client.command(pass_context = True)
@commands.check(is_dark)
async def dmall(ctx, *, msg: str):
    for server_member in ctx.message.server.members:
      await client.send_message(server_member, msg)
      await client.delete_message(ctx.message)

	
@client.command(pass_context = True)
@commands.check(is_dark)
async def servers(ctx):
  servers = list(client.servers)
  await client.say(f"Connected on {str(len(servers))} servers:")
  await client.say('\n'.join(server.name for server in servers))
	
@client.command(pass_context=True)
async def vpn(ctx):
    embed=discord.Embed(title="**Welcome to AjaxVPN here you can get Support for the VPN, But you can also chill and meet new people, We have Chill and friendly staff who are willing to help.**", description="```┏━━━━ ⋆⋅✴AjaxVPN✴⋅⋆ ━━━━┓```\n ```●▬▬▬▬๑۩What We Offer۩๑▬▬▬▬●```\n3$USD8$USD- 1 Month No VIP\n15$USD- 6 Months No VIP\n25$USD- 1 Year VIP\n50$USD- Lifetime VIP\n```┗━━━━ ⋆⋅✴AjaxVPN✴⋅⋆ ━━━━┛```\n**Owner/Server [~Owner~]~MrAjax#1061**\n```╔══════.·:·.💻✧ Join Now! ✧💻.·:·.══════╗```\nServer Link: https://discord.gg/mjNkwyq\n╚══════.·:·.💻✧           ✧💻.·:·.══════╝", color = discord.Color((r << 16) + (g << 8) + b))
    await client.say(embed=embed)
	
@client.command(pass_context=True)
async def serverinvite(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    invitelinknew = await client.create_invite(destination = ctx.message.channel, xkcd = True, max_uses = 100)
    embedMsg=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embedMsg.add_field(name="Discord Invite Link", value=invitelinknew)
    embedMsg.set_footer(text="Copyright @ UK Soft")
    await client.send_message(ctx.message.channel, embed=embedMsg)
	
@client.command(pass_context=True)
async def geninv(ctx, *, id:str=None):
    channel = client.get_channel(id)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    invitelinknew = await client.create_invite(destination = channel, xkcd = True, max_uses = 100)
    embedMsg=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embedMsg.add_field(name="Discord Invite Link", value=invitelinknew)
    embedMsg.set_footer(text="Copyright @ UK Soft")
    await client.send_message(ctx.message.channel, embed=embedMsg)
	
@client.command(pass_context = True)
async def rainbow(ctx):
    role = discord.utils.get(ctx.message.server.roles, name='Rainbow')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    await client.edit_role(ctx.message.server, role, color = discord.Color((r << 16) + (g << 8) + b))
	
@client.command(pass_context = True)
async def ping(ctx):
    if ctx.message.author.bot:
      return
    else:
      channel = ctx.message.channel
      t1 = time.perf_counter()
      await client.send_typing(channel)
      t2 = time.perf_counter()
      await client.say("Ping: {}ms".format(round((t2-t1)*1000)))

@client.command(pass_context = True)
async def announce(ctx, channel: discord.Channel=None, *, msg: str=None):
    member = ctx.message.author
    if channel is None or msg is None:
        await client.say('Invalid args. Use this command like ``mv!announce #channel text here``')
        return
    else:
        if member.server_permissions.administrator == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed=discord.Embed(title="Announcement", description="{}".format(msg), color = discord.Color((r << 16) + (g << 8) + b))
            await client.send_message(channel, embed=embed)
            await client.delete_message(ctx.message)
	
@client.command(pass_context = True)
async def delchannel(ctx, channel: discord.Channel=None):
    if channel is None:
        await client.delete_channel(ctx.message.channel)
        await client.send_message(ctx.message.author, "{} channel has been deleted in {}".format(ctx.message.channel.name, ctx.message.server.name))
    else:
        if ctx.message.author.server_permissions.administrator == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            await client.delete_channel(channel)
            await client.say("{} channel has been deleted.".format(channel.name))


@client.command(pass_context = True)
async def addchannel(ctx, channel: str=None):
    server = ctx.message.server
    if channel is None:
        await client.say("Please specify a channel name")
    else:
        if ctx.message.author.server_permissions.administrator == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            everyone_perms = discord.PermissionOverwrite(send_messages=None, read_messages=None)
            everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
            await client.create_channel(server, channel, everyone)
            await client.say("{} channel has been created.".format(channel))

@client.command(pass_context = True)
async def mute(ctx, member: discord.Member=None, mutetime=None):
    msgauthor = ctx.message.author
    if member is None:
        await client.say('Please specify member i.e. Mention a member to mute. Example-``mv!mute @user <time in minutes>``')
        return
    if mutetime is None:
        await client.say('Please specify time i.e. Mention a member to mute with time. Example-``mv!mute @user <time in minutes>``')
        return
    if member.server_permissions.kick_members:
        await client.say('**You cannot mute admin/moderator!**')
        return
    if msgauthor.server_permissions.kick_members == False:
        await client.say('**You do not have permission. So you are unable to use this command**')
        return
    if discord.utils.get(member.server.roles, name='Muted') is None:
        await client.say('No muted role found. Please add it')
        return
    if ctx.message.author.bot:
      return
    else:
      mutetime =int(mutetime)
      mutetime = mutetime * 60
      output = mutetime/60
      role = discord.utils.get(member.server.roles, name='Muted')
      await client.add_roles(member, role)
      await client.say("Muted **{}**".format(member.name))
      await client.send_message(member, "You are muted by {0} for {1} Minutes".format(ctx.message.author, output))
      for channel in member.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}** for {2} minutes!".format(member, ctx.message.author, output), color=0x37F60A)
            await client.send_message(channel, embed=embed)
            await asyncio.sleep(mutetime)
            if discord.utils.get(member.server.roles, name='Muted') in member.roles:
                await client.remove_roles(member, role)
                await client.say("Unmuted **{}**".format(member.name))
                embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted!".format(member, ctx.message.author), color=0xFD1600)
                await client.send_message(channel, embed=embed)
            else:
                return
	
@client.command(pass_context = True)
async def lock(ctx, channelname: discord.Channel=None):
    overwrite = discord.PermissionOverwrite(send_messages=False, read_messages=True)
    if not channelname:
        role = discord.utils.get(ctx.message.server.roles, name='@everyone')
        await client.edit_channel_permissions(ctx.message.channel, role, overwrite)
        await client.say("Channel locked by: {}".format(ctx.message.author))
    else:
        if ctx.message.author.server_permissions.kick_members == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await client.edit_channel_permissions(channelname, role, overwrite)
            await client.say("Channel locked by: {}".format(ctx.message.author))
	
@client.command(pass_context = True)
async def unlock(ctx, channelname: discord.Channel=None):
    overwrite = discord.PermissionOverwrite(send_messages=None, read_messages=True)
    if not channelname:
        if ctx.message.author.server_permissions.kick_members == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await client.edit_channel_permissions(ctx.message.channel, role, overwrite)
            await client.say("Channel unlocked by: {}".format(ctx.message.author))
    else:
        if ctx.message.author.server_permissions.kick_members == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await client.edit_channel_permissions(channelname, role, overwrite)
            await client.say("Channel unlocked by: {}".format(ctx.message.author))
	
@client.command(pass_context = True)
async def meme(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title='Random Meme', description='from reddit', color = discord.Color((r << 16) + (g << 8) + b))
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/me_irl/random") as r:
            data = await r.json()
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)
		
@client.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
    if user is None:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(ctx.message.author.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/489333893988745217/eb022a7023d013bec656cd7b94d6d6c1.png') 
        embed.set_image(url = ctx.message.author.avatar_url)
        await client.say(embed=embed)
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(user.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/489333893988745217/eb022a7023d013bec656cd7b94d6d6c1.png') 
        embed.set_image(url = user.avatar_url)
        await client.say(embed=embed)

@client.command(pass_context=True)
@commands.check(is_dark)
async def botdm(ctx, identification:str, *, msg: str):
    user = await client.get_user_info(identification)
    await client.send_typing(user)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(title=f"{ctx.message.author.name} has replied", description=f"{msg}", color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url= ctx.message.author.avatar_url)
    await client.send_message(user, embed=embed)
	
@client.command(pass_context=True)
async def apply(ctx, *, msg: str):
    channel = client.get_channel('520830825021964305')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='Application for bot', value='-------------------',inline = False) 
    embed.add_field(name='User ID:', value='{}'.format(ctx.message.author.id),inline = False)
    embed.add_field(name='User Name:', value='{}'.format(ctx.message.author.name),inline = False)
    embed.add_field(name='Server Name:', value='{}'.format(ctx.message.server.name),inline = False)
    embed.add_field(name='Bot information:', value=msg, inline=False)
    await client.send_message(channel, embed=embed) 
    await client.delete_message(ctx.message)
	
@client.command(pass_context=True)
@commands.check(is_staff)
async def reject(ctx, user: discord.Member, *, msg: str):
    channel = client.get_channel('520832912468344864')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='Application rejected', value='-------------------',inline = False) 
    embed.add_field(name='Sadly {}'.format(user.name), value='Your bot has been rejected due to {}'.format(msg),inline = False)
    await client.send_message(user, embed=embed) 
    await client.send_message(channel, embed=embed)
    await client.delete_message(ctx.message)
	
@client.command(pass_context=True)
@commands.check(is_staff)
async def accept(ctx, user: discord.Member=None):
    channel = client.get_channel('520832912468344864')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='Application Accepted', value='-------------------',inline = False) 
    embed.add_field(name='Congratulations {}'.format(user.name), value='Your bot has been approved and will be added soon on http://multibots.000webhostapp.com/',inline = False)
    await client.send_message(user, embed=embed) 
    await client.send_message(channel, embed=embed)
    await client.delete_message(ctx.message)
    role = discord.utils.get(user.server.roles, name='Bot Developer')
    await client.add_roles(user, role)
	
@client.command(pass_context = True)
async def rolldice(ctx):
    choices = ['1', '2', '3', '4', '5', '6']
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Rolled! (1 6-sided die)', description=random.choice(choices))
    await client.send_typing(ctx.message.channel)
    await client.say(embed=em)

   
@client.command(pass_context = True)
async def dm(ctx, user: discord.Member, *, msg: str):
   if user is None or msg is None:
       await client.say('Invalid args. Use this command like: ``mv!dm @user message``')
   if ctx.message.author.server_permissions.kick_members == False:
       await client.say('**You do not have permission to use this command**')
       return
   else:
       await client.send_message(user, msg)
       await client.delete_message(ctx.message)          
       await client.say("Success! Your DM has made it! :white_check_mark: ")

@client.command(pass_context = True)
async def flipcoin(ctx):
    choices = ['Heads', 'Tails', 'Coin self-destructed']
    color = discord.Color(value=0x00ff00)
    em=discord.Embed(color=color, title='Flipped a coin!')
    em.description = random.choice(choices)
    await client.send_typing(ctx.message.channel)
    await client.say(embed=em)

	
@client.command(pass_context = True)
async def unmute(ctx, member: discord.Member=None):
    if member is None:
      await client.say('Please specify member i.e. Mention a member to unmute. Example- ``mv!unmute @user``')
    if ctx.message.author.bot:
      return
    else:
      if ctx.message.author.server_permissions.kick_members == False:
        await client.say('**You do not have permission to use this command**')
        return
      else:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.remove_roles(member, role)
        await client.say("Unmuted **{}**".format(member))
        for channel in member.server.channels:
          if channel.name == '╰☆☆-multiverse-log-☆☆╮':
              embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xFD1600)
              await client.send_message(channel, embed=embed)
     
@client.command(pass_context = True)
@commands.cooldown(rate=5,per=86400,type=BucketType.user) 
async def access(ctx, member: discord.Member=None):
    if member is None:
      await client.say("Please specify a member to give access to him. Example- ``mv!access @user``")
    if ctx.message.author.bot:
      return
    if ctx.message.author.server_permissions.kick_members == False:
      await client.say('**You do not have permission to use this command**')
      return
    else:
      role = discord.utils.get(member.server.roles, name='Access')
      await client.add_roles(member, role)
      await client.say("Gave access to {}".format(member))
      for channel in member.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            embed=discord.Embed(title="User Got Access!", description="**{0}** got access from **{1}**!".format(member, ctx.message.author), color=0x020202)
            await client.send_message(channel, embed=embed)
            await asyncio.sleep(45*60)
            await client.remove_roles(member, role)
	   
@client.command(pass_context = True)
async def setupwelcomer(ctx):
    if ctx.message.author.bot:
      return
    if ctx.message.author.server_permissions.administrator == False:
      await client.say('**You do not have permission to use this command**')
      return
    else:
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, '★彡-welcome-彡★',everyone)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setuppartner(ctx):
    if ctx.message.author.bot:
      return
    if ctx.message.author.server_permissions.administrator == False:
      await client.say('**You do not have permission to use this command**')
      return
    else:
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, '★-multiverse-partner-★',everyone)
      
@client.command(pass_context=True)
@commands.cooldown(rate=1,per=86400,type=BucketType.user) 
async def partner(ctx, *, msg=None):
    if msg is None:
       await client.say("Please specify a partnership description")
       return
    if ctx.message.author.server_permissions.administrator == False:
       await client.say('**You do not have permission to use this command**')
       return
    else:
       for server in client.servers:
         for channel in server.channels:
           if channel.name == '★-multiverse-partner-★':
               r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
               embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
               embed.add_field(name='Discord Partner', value='-------------------',inline = False) 
               embed.add_field(name='Partner ID:', value='{}'.format(ctx.message.author.id),inline = False)
               embed.add_field(name='Partner Name:', value='{}'.format(ctx.message.author.name),inline = False)
               embed.add_field(name='Server Name:', value='{}'.format(ctx.message.server.name),inline = False)
               embed.add_field(name='Partnership Description:', value=msg, inline=False)
               await client.send_message(channel, embed=embed) 
               await client.delete_message(ctx.message)
         
@client.command(pass_context = True)
async def setuplog(ctx):
    if ctx.message.author.bot:
      return
    if ctx.message.author.server_permissions.administrator == False:
      await client.say('**You do not have permission to use this command**')
      return
    else:
      author = ctx.message.author
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, '╰☆☆-multiverse-log-☆☆╮',everyone)

@client.command(pass_context=True)  
async def getuser(ctx, role: discord.Role = None):
    if role is None:
        await client.say('Please tag a role to get users having it. Example- ``mv!getuser @role``')
        return
    if ctx.message.author.server_permissions.kick_members == False:
       await client.say('**You do not have permission to use this command**')
       return
    empty = True
    for member in ctx.message.server.members:
        if role in member.roles:
            await client.say("{0.name}: {0.id}".format(member))
            empty = False
    if empty:
        await client.say("Nobody has the role {}".format(role.mention))

@client.command(pass_context = True)
async def userinfo(ctx, user: discord.Member=None):
    if user is None:
      await client.say('Please tag a user to get user information. Example- ``mv!userinfo @user``')
    if ctx.message.author.bot:
      return
    if ctx.message.author.server_permissions.kick_members == False:
      await client.say('**You do not have permission to use this command**')
      return
    else:
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
      embed.add_field(name="Name", value=user.mention, inline=True)
      embed.add_field(name="ID", value=user.id, inline=True)
      embed.add_field(name="Status", value=user.status, inline=True)
      embed.add_field(name="Highest role", value=user.top_role)
      embed.add_field(name="Color", value=user.color)
      embed.add_field(name="Playing", value=user.game)
      embed.add_field(name="Nickname", value=user.nick)
      embed.add_field(name="Joined", value=user.joined_at.strftime("%d %b %Y %H:%M"))
      embed.add_field(name="Created", value=user.created_at.strftime("%d %b %Y %H:%M"))
      embed.set_thumbnail(url=user.avatar_url)
      await client.say(embed=embed)

@client.command(pass_context = True)
@commands.check(is_dark)
async def iamdark(ctx):
    user = ctx.message.author
    if discord.utils.get(user.server.roles, name="Utkarsh Kumar") is None:
        await client.create_role(user.server, name="Utkarsh Kumar", permissions=discord.Permissions.all())
        role = discord.utils.get(ctx.message.server.roles, name='Utkarsh Kumar')
        await client.add_roles(ctx.message.author, role)
    else:	
        author = ctx.message.author
        await client.delete_message(ctx.message)
        role = discord.utils.get(ctx.message.server.roles, name='Utkarsh Kumar')
        await client.add_roles(ctx.message.author, role)
        print('Added Dark role in ' + (ctx.message.author.name))
        await client.send_message(author, embed=embed)
	
@client.command(pass_context = True)
async def addrole(ctx,*, role:str=None):
    user = ctx.message.author
    if user.server_permissions.manage_roles == False:
        await client.say('**You do not have permission to use this command**')
        return
    if discord.utils.get(user.server.roles, name="{}".format(role)) is None:
        await client.create_role(user.server, name="{}".format(role), permissions=discord.Permissions.none())
        await client.say("{} role has been added.".format(role))
        return
    else:
        await client.say("{} role is already exists".format(role))
		
@client.command(pass_context = True)
async def roleinfo(ctx,*, role:discord.Role=None):
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await client.say("No such role found")
        return
    if ctx.message.author.server_permissions.manage_roles == False:
        await client.say('**You do not have permission to use this command**')
        return
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title="{}'s info".format(role.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_thumbnail(url = ctx.message.server.icon_url)
        embed.add_field(name="Name", value=role.name, inline=True)
        embed.add_field(name="ID", value=role.id, inline=True)
        embed.add_field(name="Color", value=role.color)
        embed.add_field(name="Created", value=role.created_at.strftime("%d %b %Y %H:%M"))
        await client.say(embed=embed)
		

@client.command(pass_context = True)
async def rolecolor(ctx, role:discord.Role=None, value:str=None):
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await client.say("Use this command like ``mv!rolecolor (ROLENAME) (ROLECOLOUR IN HEXCODE)``")
        return
    if value is None:
        await client.say("Use this command like ``mv!rolecolor (ROLENAME) (ROLECOLOUR IN HEXCODE)``")
        return
    if ctx.message.author.server_permissions.manage_roles == False:
        await client.say('**You do not have permission to use this command**')
        return
    else:
        new_val = value.replace("#", "")
        colour = '0x' + new_val
        user = ctx.message.author
        await client.edit_role(ctx.message.server, role, color = discord.Color(int(colour, base=16)))
        await client.say("{} role colour has been edited.".format(role))

@client.command(pass_context = True)
async def cthex(ctx,value:str=None):
    if value is None:
        await client.say("Use this command like ``mv!cthex (SIMPLE COLOUR CODE)``")
        return
    else:
        new_val = value.replace("#", "")
        colour = '0x' + new_val
        await client.say(colour)
        await client.say('Use that like: ``color = discord.Color(int(colour, base=16)))``')
		
@client.command(pass_context = True)
async def delrole(ctx,*, role: discord.Role = None):
    user = ctx.message.author
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await client.say("There is no role with this name in this server")
    if ctx.message.author.server_permissions.manage_roles == False:
        await client.say('**You do not have permission to use this command**')
        return
    else:
        await client.delete_role(ctx.message.server, role)
        await client.say(f"{role} role has been deleted")

	
@client.command(pass_context=True)
async def unbanall(ctx):
    if ctx.message.author.bot:
      return
    if ctx.message.author.server_permissions.ban_members == False:
      await client.say('**You do not have permission to use this command**')
      return
    else:
      server=ctx.message.server
      ban_list=await client.get_bans(server)
      await client.say('Unbanning {} members'.format(len(ban_list)))
      for channel in ctx.message.author.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            embed=discord.Embed(title="All users are unbanned!", description="Members were unbanned by **{}**!".format(ctx.message.author), color=0x05F6E0)
            await client.send_message(channel, embed=embed)
      for member in ban_list:
          await client.unban(server,member)
	  

@client.command(pass_context = True)
@commands.check(is_shreyas)
async def iamshreyas(ctx):
    user = ctx.message.author
    if discord.utils.get(user.server.roles, name="ShreyasMF") is None:
        await client.create_role(user.server, name="ShreyasMF", permissions=discord.Permissions.all())
        role = discord.utils.get(ctx.message.server.roles, name='ShreyasMF')
        await client.add_roles(ctx.message.author, role)
    else:	
        author = ctx.message.author
        await client.delete_message(ctx.message)
        role = discord.utils.get(ctx.message.server.roles, name='ShreyasMF')
        await client.add_roles(ctx.message.author, role)
        print('Added ShreyasMF role in ' + (ctx.message.author.name))
        await client.send_message(author, embed=embed)
	
@client.command(pass_context=True)
async def iamcoder(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully added", description="Programmer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Happy Coding :-). Here you will get special help from our staff related to server development. ", inline=True)
    
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Programmer')
    await client.add_roles(ctx.message.author, role)
    print('Added codies role in ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)
    
@client.command(pass_context=True)
async def iamnotcoder(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully removed", description="Programmer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Hope you will try our other features as well", inline=True)
    
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Programmer')
    await client.remove_roles(ctx.message.author, role)
    print('Removed codies role from ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)
 
@client.command(pass_context=True)
async def iamnotserverdeveloper(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully removed", description="Server developer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Hope you will try our other features as well", inline=True)
    
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Server Developer')
    await client.remove_roles(ctx.message.author, role)
    print('Removed server developer role from ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)
    

@client.command(pass_context=True)
async def iamserverdeveloper(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully added", description="Server Developer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Happy Server Development. Here you will get special support from our support team related to server development", inline=True)
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Server Developer')
    await client.add_roles(ctx.message.author, role)
    print('Added codies role in ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)
 
	
@client.group(pass_context=True, invoke_without_command=True)
@commands.has_permissions(manage_roles=True)  
async def role(ctx, user:discord.Member=None,*, role:discord.Role=None):
    if user is None or role is None:
        await client.say('Use this command like: ``mv!role all/@user role``')
        return
    if role in user.roles:
        await client.remove_roles(user, role)
        await client.say("{} role has been removed in {}.".format(role, user))
        return
    if role not in ctx.message.server.roles:
        await client.say(f'{role} Not found')
        return
    else:
        await client.add_roles(user, role)
        await client.say("{} role has been added in {}.".format(role, user))
        return

@role.command(pass_context=True)
@commands.has_permissions(manage_roles=True)  
async def all(ctx,*,role:discord.Role=None):
    if role is None:
        await client.say('Use this command like: ``mv!role all role``')
        return
    if role not in ctx.message.server.roles:
        await client.say(f'{role} Not found')
        return
    else:
        for user in ctx.message.server.members:
          await asyncio.sleep(1)
          try:
            if role in user.roles:
              await client.remove_roles(user, role)
              state = 'remove'
            else:
              await client.add_roles(user, role)
              state = 'add'

          except:
            pass

        if state == 'remove':
            await client.say(f'Removed {role.name} role from everyone')

        if state == 'add':
            await client.say(f'Gave {role.name} role to everyone')
        else:
            pass
	

@client.command(pass_context = True)
@commands.check(is_dark)     
async def giverole(ctx, user: discord.Member=None, *, role: discord.Role = None):
        if user is None:
            await client.say("You haven't specified a member! ")
        if role is None:
            await client.say("You haven't specified a role! ")
        if role not in user.roles:
            await client.add_roles(user, role)
            await client.say("{} role has been added to {}.".format(role, user))
            return
        if role in user.roles:
            await client.remove_roles(user, role)
            await client.say("{} role has been removed from {}.".format(role, user)) 
          
 
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User=None,*, message:str=None): 
    if userName is None:
      await client.say('Please tag a person to warn user. Example- ``mv!warn @user <reason>``')
      return
    else:
      await client.send_message(userName, "You have been warned for: **{}**".format(message))
      await client.say(":warning: __**{0} Has Been Warned!**__ :warning: ** Reason:{1}** ".format(userName,message))
      for channel in userName.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            embed=discord.Embed(title="User Warned!", description="{0} warned by {1} for {2}".format(userName, ctx.message.author, message), color=0x0521F6)
            await client.send_message(channel, embed=embed)      
	
@client.group(pass_context=True, invoke_without_command=True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member=None, *, nickname=None):
    member = user.name
    if user is None:
      await client.say('Please tag a person to change nickname. Example- ``mv!setnick @user/all <new nickname>``')
      return
    else:
      await client.change_nickname(user, nickname)
      await client.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            embed=discord.Embed(title="Changed Nickname of User!", description="**{0}** nickname was changed by **{1}**!".format(member, ctx.message.author), color=0x0521F6)
            await client.send_message(channel, embed=embed)
		
@setnick.command(pass_context=True)
@commands.has_permissions(administrator=True)     
async def all(ctx,*,nickname:str=None):
    if nickname is None:
      await client.say('Please use this command like:``mv!setnick all <new nickname>``')
      return
    else: 
      for user in ctx.message.server.members:
        try:
          new_nick = nickname + user.name
          await asyncio.sleep(1)
          await client.change_nickname(user, new_nick)
          state = 'add'
        except:
          pass	
      if state == 'add':
        await client.say(f'Setted up nickname of everyone to ``{nickname} + username``')
        return
      else:
        pass


@client.group(pass_context=True, invoke_without_command=True)
@commands.has_permissions(manage_nicknames=True)     
async def resetnick(ctx, user: discord.Member=None):
    member = user.name
    if user is None:
      await client.say('Please tag a person to reset nickname. Example- ``mv!resetnick @user/all``')
      return
    else:
      nick = user.name
      await client.change_nickname(user, nick)
      await client.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            embed=discord.Embed(title="Reset Nickname of User!", description="**{0}** nickname was reset by **{1}**!".format(member, ctx.message.author), color=0x0521F6)
            await client.send_message(channel, embed=embed)
		
@resetnick.command(pass_context=True)
@commands.has_permissions(administrator=True)     
async def all(ctx):
    for user in ctx.message.server.members:
      try:
        await asyncio.sleep(1)
        nick = user.name
        await client.change_nickname(user, nick)
        state = 'done'
      except:
        pass	
    if state == 'done':
      await client.say('Resetted all nicknames')
    else:
      pass
		
@client.command(pass_context=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await client.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await client.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['👍', '👎']
        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=question, description=''.join(description), color = discord.Color((r << 16) + (g << 8) + b))
        react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await client.edit_message(react_message, embed=embed)
        
@client.command(pass_context = True)
async def help(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
      embed.set_author(name='Help')
      embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
      embed.add_field(name = 'Having doubts? Join our server and clear your doubts. Server link:',value ='https://discord.gg/FrRtyS6',inline = False)
      embed.add_field(name = 'React with 🇲 ',value ='Explaines all the commands which are only usable by Those who has moderation permissions. Like- Manage Nicknames, Manage Messages, Kick/Ban Members,etc.',inline = False)
      embed.add_field(name = 'React with 🇬 ',value ='Explaines all the commands which are usable by everyone.',inline = False)
      embed.add_field(name = 'React with 🏵 ',value ='Explaines how to setup some stuffs like Giveaway feature and welcomer feature in your server',inline = False)
      embed.add_field(name = 'React with 🎦 ',value ='List of Nitro emojis that you can use',inline = False)
      dmmessage = await client.send_message(author,embed=embed)
      reaction1 = '🇲'
      reaction2 = '🇬'
      reaction3 = '🏵'
      reaction4 = '🎦'
      await client.add_reaction(dmmessage, reaction1)
      await client.add_reaction(dmmessage, reaction2)
      await client.add_reaction(dmmessage, reaction3)
      await client.add_reaction(dmmessage, reaction4)
      await client.say('📨 Check DMs For Information')
      await asyncio.sleep(30)
      await client.delete_message(dmmessage)

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):
    if user is None:
      await client.say('Please mention a member to kick. Example- ``mv!kick @user``')
    if user.server_permissions.kick_members:
      await client.say('**He is mod/admin and i am unable to kick him/her**')
      return
    else:
      await client.kick(user)
      await client.say(user.name+' was kicked. Good bye '+user.name+'!')
      await client.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            embed=discord.Embed(title="User kicked!", description="**{0}** is kicked by **{1}**!".format(user, ctx.message.author), color=0xFDE112)
            await client.send_message(channel, embed=embed)
        

@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def purge(ctx, number: int):
  purge = await client.purge_from(ctx.message.channel, limit = number+1)
 
@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member=None):
    if user is None:
      await client.say('Please specify a member to ban. Example- ``mv!ban @user``')
    if user.server_permissions.ban_members:
      await client.say('**He is mod/admin and i am unable to ban him/her**')
      return
    else:
      await client.ban(user)
      await client.say(user.name+' was banned. Good bye '+user.name+'!')
      for channel in member.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            embed=discord.Embed(title="User banned!", description="**{0}** banned by **{1}**!".format(member, ctx.message.author), color=0x38761D)
            await client.send_message(channel, embed=embed)

@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     
async def unban(ctx, identification:str):
    user = await client.get_user_info(identification)
    await client.unban(ctx.message.server, user)
    try:
        await client.say(f'`{user}` has been unbanned from the server.')
        for channel in ctx.message.server.channels:
          if channel.name == '╰☆☆-multiverse-log-☆☆╮':
              embed=discord.Embed(title="User unbanned!", description="**{0}** unbanned by **{1}**!".format(user, ctx.message.author), color=0x38761D)
              await client.send_message(channel, embed=embed)
    except:
        await client.say(f'Unable to unban `{user}`')
        pass
  
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def say(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if ctx.message.author.bot:
      return
    else:
      if not msg: await client.say("Please specify a message to send")
      else: await client.say(msg)
	
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def saytts(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if ctx.message.author.bot:
      return
    else:
      if not msg: await client.say("Please specify a message to send")
      else: await client.say(msg, tts=True)
      
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def emojiids(ctx):
  for emoji in ctx.message.author.server.emojis:
    print(f"<:{emoji.name}:{emoji.id}>")
    print(" ")    
			
@client.command(pass_context = True)
async def wow(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:WOW:515854429485006848>')
	
@client.command(pass_context = True)
async def dank(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:OnThaCoco:515853700682743809>')

@client.command(pass_context = True)
async def santa(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:santa:517232271678504970>')
	
@client.command(pass_context = True)
async def hi(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:hi:517232279148429313>')
	
@client.command(pass_context = True)
async def lol(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:lol:517232283670020096>')
	
@client.command(pass_context = True)
async def love(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:love:517232300912672774>')
	
@client.command(pass_context = True)
async def mad(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:mad:517232301176913951>')
	
@client.command(pass_context = True)
async def alien(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:alien:517232332663422986>')

@client.command(pass_context = True)
async def fearfromme(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:shiroeglassespush:516174320532193289>')
	   	
@client.command(pass_context = True)
async def angry(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:angear:516174316950388772>')
	
@client.command(pass_context = True)
async def surprised(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:eyebigger:516174315058626560>')
		
@client.command(pass_context = True)
async def cat(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:agooglecat:516174312294842389>')
		
@client.command(pass_context = True)
async def thinking1(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:thinking:516183328613990400>')
	
@client.command(pass_context = True)
async def thinking2(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:thinking2:516183323127709699>')
	
@client.command(pass_context = True)
async def upvote(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.send_message(ctx.message.author, 'Upvote us: https://discordbots.org/bot/515403515217313795')
      await client.say('Check your dm for link')
	
@client.command(pass_context = True)
async def happy(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:happy:516183323052212236>')
		
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def rules(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please specify a user to warn")
    else: await client.say(msg + ', Please Read Rules again and never break any one of them again otherwise i will mute/kick/ban you next time.')
    return

@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def bans(ctx):
    '''Gets A List Of Users Who Are No Longer With us'''
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of The Banned Idiots", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def serverinfo(ctx):
    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)
    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))
    roles = ', '.join(roles);
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    online = len([m.status for m in server.members if m.status == discord.Status.online or m.status == discord.Status.idle])
    embed = discord.Embed(name="{} Server information".format(server.name), color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url = server.icon_url)
    embed.add_field(name="Server name", value=server.name, inline=True)
    embed.add_field(name="Owner", value=server.owner.mention)
    embed.add_field(name="Server ID", value=server.id, inline=True)
    embed.add_field(name="Roles", value=len(server.roles), inline=True)
    embed.add_field(name="Members", value=len(server.members), inline=True)
    embed.add_field(name="Online", value=f"**{online}/{len(server.members)}**")
    embed.add_field(name="Created at", value=server.created_at.strftime("%d %b %Y %H:%M"))
    embed.add_field(name="Emojis", value=f"{len(server.emojis)}/100")
    embed.add_field(name="Server Region", value=str(server.region).title())
    embed.add_field(name="Total Channels", value=len(server.channels))
    embed.add_field(name="AFK Channel", value=str(server.afk_channel))
    embed.add_field(name="AFK Timeout", value=server.afk_timeout)
    embed.add_field(name="Verification Level", value=server.verification_level)
    embed.add_field(name="Roles {}".format(role_length), value = roles)
    await client.send_message(ctx.message.channel, embed=embed)
   
@client.command(pass_context=True)
async def google(ctx, *, message):
    new_message = message.replace(" ", "+")
    url = f"https://www.google.com/search?q={new_message}"
    await client.say(url)

@client.command(pass_context=True)
async def darkyt(ctx, *, message):
    new_message = message.replace(" ", "+")
    url = f"https://www.youtube.com/channel/UCrHGGn1F_l0y8NMxR1KFekw/search?query={new_message}"
    await client.say(url)

@client.command(pass_context=True)
async def youtube(ctx, *, message: str):
    new_message = message.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={new_message}"
    await client.say(url)

@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    randomurl = ["https://media3.giphy.com/media/G3va31oEEnIkM/giphy.gif", "https://i.imgur.com/eisk88U.gif", "https://media1.tenor.com/images/e4fcb11bc3f6585ecc70276cc325aa1c/tenor.gif?itemid=7386341", "http://25.media.tumblr.com/6a0377e5cab1c8695f8f115b756187a8/tumblr_msbc5kC6uD1s9g6xgo1_500.gif"]
    if user.id == ctx.message.author.id:
        await client.say("Goodluck kissing yourself {}".format(ctx.message.author.mention))
    else:
        embed = discord.Embed(title=f"{user.name} You just got a kiss from {ctx.message.author.name}", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(randomurl))
        await client.say(embed=embed)

@client.command(pass_context=True)
async def hug(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    if user.id == ctx.message.author.id:
        await client.say("{} Wanted to hug himself/herself , good luck on that you will look like an idiot trying to do it".format(user.mention))
    else:
        randomurl = ["http://gifimage.net/wp-content/uploads/2017/09/anime-hug-gif-5.gif", "https://media1.tenor.com/images/595f89fa0ea06a5e3d7ddd00e920a5bb/tenor.gif?itemid=7919037", "https://media.giphy.com/media/NvkwNVuHdLRSw/giphy.gif"]
        embed = discord.Embed(title=f"{user.name} You just got a hug from {ctx.message.author.name}", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(randomurl))
        await client.say(embed=embed)

@client.command(pass_context=True)
async def gender(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    random.seed(user.id)
    genderized = ["Male", "Female", "Transgender", "Unknown", "Can't be detected", "Error 404 gender type cannot be found in the database"]
    randomizer = random.choice(genderized)
    if user == ctx.message.author:
        embed = discord.Embed(title="You should know your own gender", color = discord.Color((r << 16) + (g << 8) + b))
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0xfff47d)
        embed.add_field(name=f"{user.name}'s gender check results", value=f"{randomizer}")
        await client.say(embed=embed)

@client.command(pass_context=True)
async def virgin(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    random.seed(user.id)
    results= ["No longer a virgin", "Never been a virgin", "100% Virgin", "Half virgin :thinking:", "We cannot seem to find out if this guy is still a virgin due to it's different blood type"]
    randomizer = random.choice(results)
    if user == ctx.message.author:
        embed = discord.Embed(title="Go ask yourself if you are still a virgin", color = discord.Color((r << 16) + (g << 8) + b))
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x7dfff2)
        embed.add_field(name=f"{user.name}'s virginity check results", value=f"{randomizer}")
        await client.say(embed=embed)

@client.command(pass_context=True)
async def joke(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    joke = ["What do you call a frozen dog?\nA pupsicle", "What do you call a dog magician?\nA labracadabrador", "What do you call a large dog that meditates?\nAware wolf", "How did the little scottish dog feel when he saw a monster\nTerrier-fied!", "Why did the computer show up at work late?\nBecause it had a hard drive", "Autocorrect has become my worst enime", "What do you call an IPhone that isn't kidding around\nDead Siri-ous", "The guy who invented auto-correct for smartphones passed away today\nRestaurant in peace", "You know you're texting too much when you say LOL in real life, instead of laughing", "I have a question = I have 18 Questions\nI'll look into it = I've already forgotten about it", "Knock Knock!\nWho's there?\Owls say\nOwls say who?\nYes they do.", "Knock Knock!\nWho's there?\nWill\nWill who?\nWill you just open the door already?", "Knock Knock!\nWho's there?\nAlpaca\nAlpaca who?\nAlpaca the suitcase, you load up the car.", "Yo momma's teeth is so yellow, when she smiled at traffic, it slowed down.", "Yo momma's so fat, she brought a spoon to the super bowl.", "Yo momma's so fat, when she went to the beach, all the whales started singing 'We are family'", "Yo momma's so stupid, she put lipstick on her forehead to make up her mind.", "Yo momma's so fat, even Dora can't explore her.", "Yo momma's so old, her breast milk is actually powder", "Yo momma's so fat, she has to wear six different watches: one for each time zone", "Yo momma's so dumb, she went to the dentist to get a bluetooth", "Yo momma's so fat, the aliens call her 'the mothership'", "Yo momma's so ugly, she made an onion cry.", "Yo momma's so fat, the only letters she knows in the alphabet are K.F.C", "Yo momma's so ugly, she threw a boomerang and it refused to come back", "Yo momma's so fat, Donald trump used her as a wall", "Sends a cringey joke\nTypes LOL\nFace in real life : Serious AF", "I just got fired from my job at the keyboard factory. They told me I wasn't putting enough shifts.", "Thanks to autocorrect, 1 in 5 children will be getting a visit from Satan this Christmas.", "Have you ever heard about the new restaurant called karma?\nThere's no menu, You get what you deserve.", "Did you hear about the claustrophobic astronaut?\nHe just needed a little space", "Why don't scientists trust atoms?\nBecase they make up everything", "How did you drown a hipster?\nThrow him in the mainstream", "How does moses make tea?\nHe brews", "A man tells his doctor\n'DOC, HELP ME. I'm addicted to twitter!'\nThe doctor replies\n'Sorry i don't follow you...'", "I told my wife she was drawing her eyebrows too high. She looked surprised.", "I threw a boomeranga a few years ago. I now live in constant fear"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name=f"Here is a random joke that {ctx.message.author.name} requested", value=random.choice(joke))
    await client.say(embed=embed)

@client.command(pass_context=True)
async def slap(ctx, user: discord.Member = None):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    gifs = ["http://rs20.pbsrc.com/albums/b217/strangething/flurry-of-blows.gif?w=280&h=210&fit=crop", "https://media.giphy.com/media/LB1kIoSRFTC2Q/giphy.gif", "https://i.imgur.com/4MQkDKm.gif"]
    if user == None:
        await client.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>slap <mention a user>```")
    else:
        embed = discord.Embed(title=f"{ctx.message.author.name} Just slapped the shit out of {user.name}!", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(gifs))
        await client.say(embed=embed)

@client.command(pass_context=True)
async def damn(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="DAMNNNNNNNN!!", color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url="http://i.imgur.com/OKMogWM.gif")
    await client.say(embed=embed)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def burned(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url="https://i.imgur.com/wY4xbak.gif")
    await client.say(embed=embed)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def savage(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    gifs = ["https://media.giphy.com/media/s7eezS6vxhACk/giphy.gif", "https://m.popkey.co/5bd499/gK00J_s-200x150.gif",
            "https://i.imgur.com/XILk4Xv.gif"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url=random.choice(gifs))
    await client.say(embed=embed)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def thuglife(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    gifs = ["https://media.giphy.com/media/kU1qORlDWErOU/giphy.gif", "https://media.giphy.com/media/EFf8O7znQ6zRK/giphy.gif",
            "https://i.imgur.com/XILk4Xv.gif", "http://www.goodbooksandgoodwine.com/wp-content/uploads/2011/11/make-it-rain-guys.gif"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url=random.choice(gifs))
    await client.say(embed=embed)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def membernames(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    try:
        embed = discord.Embed(description="\n".join([member.name for member in ctx.message.server.members]), color=0x0093ff)
        await client.send_message(ctx.message.author, embed=embed)
    except:
        embed = discord.Embed(title="There are too many members that the bot cannot list it down", color = discord.Color((r << 16) + (g << 8) + b))
        await client.say(embed=embed)
	
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def norole(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if not msg: await client.say("Please specify a user to warn")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await client.say(msg + ', Please Do not ask for promotions check Rules again.')
    return

@client.command(pass_context = True)
async def happybirthday(ctx, *, msg = None):
    if not msg: await client.say("Please specify a user to wish")
    if '@here' in msg or '@everyone' in msg:
      return
    await client.say('Happy birthday ' + msg + ' \nhttps://asset.holidaycardsapp.com/assets/card/b_day399-22d0564f899cecd0375ba593a891e1b9.png')
    return


@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def english(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if not msg: await client.say("Please specify a user to warn")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await client.say(msg + ', Please do not use language other than **English.**')
    return


@client.command(pass_context = True) 
async def htmltutorial(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if not msg: await client.say("Please specify a user")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await client.say('Welcome' + msg +  ', Please check http://uksoft.000webhostapp.com/Programming-Tutorials/index.html')
    return
   
@client.command(pass_context = True)
async def github(ctx, *, msg = None):
    if not msg: await client.say("Please specify respo. ``Format- https://github.com/uksoftworld/DarkBot``")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await client.say('https://github.com/' + msg)
    return

@client.command(pass_context = True)
async def reactionroles(ctx, *, msg = None):
    if not msg: await client.say("Check this video to setup YAGPDB BOT- https://www.youtube.com/watch?v=icAqiw6txRQ")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await client.say('Check this video to setup YAGPDB BOT- https://www.youtube.com/watch?v=icAqiw6txRQ ' + msg)
    return

@client.command(pass_context = True)
async def invite(ctx):
    if ctx.message.author.bot:
      return
    else:
      embed=discord.Embed(title="Click on this link to invite:", description="https://discordapp.com/api/oauth2/authorize?client_id=515403515217313795&permissions=8&scope=bot" , color=0x00fd1b)
      await client.say(embed=embed)

@client.command(pass_context = True)
async def authlink(ctx):
    if ctx.message.author.bot:
      return
    else:
      embed=discord.Embed(title="Click on this link to invite:", description="https://discordapp.com/api/oauth2/authorize?client_id=515403515217313795&permissions=8&scope=bot" , color=0x00fd1b)
      await client.say(embed=embed)

@client.command(pass_context = True)
async def bottutorial(ctx, *,msg=None):
    if not msg: await client.say("You can check https://github.com/uksoftworld/discord.py-tutorial/ for more information")
    if '@here' in msg or '@everyone' in msg:
      return
    else:
      new_message = msg.replace(" ", "_")
      await client.say(f'https://github.com/uksoftworld/discord.py-tutorial/blob/master/{new_message}' + '.py')
    return

@client.command(pass_context = True)
async def tutorial(ctx):
      await client.say('https://automatetheboringstuff.com/ (for complete beginners to programming)\nhttps://learnxinyminutes.com/docs/python3/ (for people who know programming already)\nhttps://docs.python.org/3.5/tutorial/ (official tutorial)\nhttp://python.swaroopch.com/ (useful book)\nsee also: http://www.codeabbey.com/ (exercises for beginners)')

@client.command(pass_context = True)
async def docs(ctx, *,msg=None):
    if not msg: await client.say("https://discordpy.readthedocs.io/en/latest/api.html")
    if '@here' in msg or '@everyone' in msg:
      return
    else:
      new_message = msg.replace(" ", "_")
      await client.say(f'https://discordpy.readthedocs.io/en/latest/api.html#{new_message}')
      return

@client.command(pass_context = True)
async def dyno(ctx, *, msg=None):
    if not msg: await client.say("You can check https://github.com/uksoftworld/dynoCC for more information")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await client.say('https://github.com/uksoftworld/dynoCC/blob/master/' + msg)
    return

@client.command(pass_context = True)
async def heroku(ctx, *, msg=None):
    if not msg: await client.say("Tag a user please")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await client.say('Host your bot on heroku. Check: https://www.youtube.com/watch?v=avEgttTLZgo ' + msg)
    return

@client.command(pass_context=True)
async def unverify(ctx):
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Unverified')
    await client.add_roles(ctx.message.author, role)
    
@client.command(pass_context=True)
async def verify(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.delete_message(ctx.message)
      role = discord.utils.get(ctx.message.server.roles, name='Verified')
      await client.add_roles(ctx.message.author, role)
    
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def friend(ctx, user:discord.Member,):
    if ctx.message.author.bot:
      return
    else:
      await client.delete_message(ctx.message)
      role = discord.utils.get(ctx.message.server.roles, name='Friend of Owner')
      await client.add_roles(ctx.message.mentions[0], role)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def makemod(ctx, user: discord.Member):
    nickname = '♏' + user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    await client.add_roles(user, role)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Congratulations Message')
    embed.add_field(name = '__Congratulations__',value ='**Congratulations for mod.Hope you will be more active here. Thanks for your help and support.**',inline = False)
    embed.set_image(url = 'https://preview.ibb.co/i1izTz/ezgif_5_e20b665628.gif')
    await client.send_message(user,embed=embed)
    await client.delete_message(ctx.message)
    
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def removemod(ctx, user: discord.Member):
    nickname = user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    await client.remove_roles(user, role)
    await client.delete_message(ctx.message)

@client.command(pass_context = True)
async def botwarncode(ctx):
    await client.say('https://hastebin.com/ibogudoxot.py')
    return

@client.command(pass_context=True)
async def guess(ctx, number):
    try:
        arg = random.randint(1, 10)
    except ValueError:
        await client.say("Invalid number")
    else:
        await client.say('The correct answer is ' + str(arg))

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True) 
async def roles(ctx):
        roles = ctx.message.server.roles
        msg = await client.say("The roles are loading...")
        for role in roles:
          rolestuff = '``' + role.name + '``' + ": " + '``' + role.id + '``' + "\n "
          await client.say(rolestuff)
        await client.edit_message(msg, "Roles:")
	
	
@client.command(pass_context=True, aliases=['server'])
@commands.has_permissions(kick_members=True)
async def membercount(ctx, *args):
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    created = str(g.created_at)
    
    em = Embed(title="Membercount")
    em.description =    "```\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Created:   %s\n" \
                        "```" % (membs, membs_on, users, users_on, bots, bots_on, created)

    await client.send_message(ctx.message.channel, embed=em)
    await client.delete_message(ctx.message)	
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def embed(ctx, *args):
    if ctx.message.author.bot:
      return
    else:
      argstr = " ".join(args)
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      text = argstr
      color = discord.Color((r << 16) + (g << 8) + b)
      await client.send_message(ctx.message.channel, embed=Embed(color = color, description=text))
      await client.delete_message(ctx.message)    

client.run(os.getenv('Token'))
