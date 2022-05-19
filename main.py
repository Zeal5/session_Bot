import discord
from dotenv import load_dotenv
import os
import time
import datetime
from discord.ext import commands , tasks

load_dotenv()
bot = commands.Bot(command_prefix='!',activity=discord.Activity(type=discord.ActivityType.watching, name="Markets"))
a = [0,1,2,3,4,5]
@bot.event
async def on_ready():
    print('We have logged in as ',bot.user)
    NY_start.start()
    NY_end.start()
    Tokyo_start.start()
    London_end.start()
    London_start.start()
    Sydney_start.start()
    Sydney_end.start()
 
#sydney_session start
@tasks.loop(hours=24)
async def Sydney_start():
    if datetime.datetime.weekday(datetime.datetime.today()) in a:
        channel = bot.get_channel(974719903443603579)
        epoch = time.time()
        epoch_1 = int(epoch) + (60*30)
        ny_message = discord.Embed(title= f' sydney-session is starting  <t:{epoch_1}:R>',color=0x96C3EB)                                              #1 sydney_start
        await channel.send(embed=ny_message)
        time.sleep(60*30)
        ny_messag = discord.Embed(title= f' sydney-session has started ',color=0x299438)
        await channel.send(embed=ny_messag)

#sydney_session end
@tasks.loop(hours=24)
async def Sydney_end():
    if datetime.datetime.weekday(datetime.datetime.today()) in a:
        channel = bot.get_channel(974719903443603579)
        epoch = time.time()
        epoch_1 = int(epoch) + (30*60)
        ny_message = discord.Embed(title= f' sydney-session is ending  <t:{epoch_1}:R>',color=0xAF38EB)                                              #2 sydney_end
        await channel.send(embed=ny_message)
        time.sleep(60*30)
        ny_messag = discord.Embed(title= f' sydney-session has ended ',color=0x14AAF5)
        await channel.send(embed=ny_messag)

#Tokyo_session_start message
@tasks.loop(hours=24)
async def Tokyo_start():
    if datetime.datetime.weekday(datetime.datetime.today()) in a:
        channel = bot.get_channel(974719903443603579)
        epoch = time.time()
        epoch_1 = int(epoch) + (60*30)
        ny_message = discord.Embed(title= f' Tokyo is starting in <t:{epoch_1}:R>',color=0x96C3EB)                                                    #7    Tokyo_start
        await channel.send(embed=ny_message)
        time.sleep(60*30)
        ny_messag = discord.Embed(title= f' Tokyo has started ',color=0x299438)
        await channel.send(embed=ny_messag)

#London_session start
@tasks.loop(hours=24)
async def London_start():
    if datetime.datetime.weekday(datetime.datetime.today()) in a:
        channel = bot.get_channel(974719903443603579)
        epoch = time.time()
        epoch_1 = int(epoch) + (30*60)
        ny_message = discord.Embed(title= f' london-session is starting and Tokyo is ending in  <t:{epoch_1}:R>',color=0x96C3EB)                                             #3 London_start
        await channel.send(embed=ny_message)
        #tokyo_end                                                   #8    Tokyo_end
        time.sleep(60*30)
        ny_messag = discord.Embed(title= f' london-session has started ',color=0x299438)
        await channel.send(embed=ny_messag)

#London_session end
@tasks.loop(hours=24)
async def London_end():
    if datetime.datetime.weekday(datetime.datetime.today()) in a:
        channel = bot.get_channel(974719903443603579)
        epoch = time.time()
        epoch_1 = int(epoch) + (30*60)
        ny_message = discord.Embed(title= f' london-session is ending  <t:{epoch_1}:R>',color=0xAF38EB)                                               #4 London_end
        await channel.send(embed=ny_message)
        time.sleep(60*30)
        ny_messag = discord.Embed(title= f' london-session has ended ',color=0x14AAF5)
        await channel.send(embed=ny_messag)

#ny_session starting message
@tasks.loop(hours=24)
async def NY_start():
    if datetime.datetime.weekday(datetime.datetime.today()) in a:
        channel = bot.get_channel(974719903443603579)
        epoch = time.time()
        epoch_1 = int(epoch) + (30*60)
        ny_message = discord.Embed(title= f' NY-session is starting  <t:{epoch_1}:R>',color=0x96C3EB)                                                #5 NY_start
        await channel.send(embed=ny_message)
        time.sleep(60*30)
        ny_messag = discord.Embed(title= f' NY-session has started ',color=0x299438)
        await channel.send(embed=ny_messag)

#NY_session end message
@tasks.loop(hours=24)
async def NY_end():
    if datetime.datetime.weekday(datetime.datetime.today()) in a:
        channel = bot.get_channel(974719903443603579)
        epoch = time.time()
        epoch_1 = int(epoch) + (30*60)
        ny_message = discord.Embed(title= f' NY-session is ending  <t:{epoch_1}:R>',color=0xAF38EB)                                                 #6  NY_end
        await channel.send(embed=ny_message)
        time.sleep(60*30)
        ny_messag = discord.Embed(title= f' NY-session has ended ',color=0x14AAF5)
        await channel.send(embed=ny_messag)




#loops for tasks
#sydney_start
@Sydney_start.before_loop
async def wait():
    sleep_time = (datetime.datetime.utcnow() + datetime.timedelta(days=1)).replace(hour=21, minute=30, second=00)      #1
    await discord.utils.sleep_until(sleep_time)

#sydney_end
@Sydney_end.before_loop
async def wait():
    sleep_time = (datetime.datetime.utcnow() + datetime.timedelta(days=1)).replace(hour=5, minute=30, second=0)       #2
    await discord.utils.sleep_until(sleep_time)

#tokyo_loop starter
@Tokyo_start.before_loop
async def wait():
    sleep_time = (datetime.datetime.utcnow() + datetime.timedelta(days=1)).replace(hour=22, minute=30, second=0)      #7
    await discord.utils.sleep_until(sleep_time)

#london_start
@London_start.before_loop
async def wait():
    sleep_time = (datetime.datetime.utcnow() + datetime.timedelta(days=1)).replace(hour=6, minute=30, second=0)       #3
    await discord.utils.sleep_until(sleep_time)

#london_end
@London_end.before_loop
async def wait():
    sleep_time = (datetime.datetime.utcnow() + datetime.timedelta(days=1)).replace(hour=14, minute=30, second=0)      #4
    await discord.utils.sleep_until(sleep_time)


#ny_start_loop starter
@NY_start.before_loop
async def wait():
    sleep_time = (datetime.datetime.utcnow() + datetime.timedelta(days=1)).replace(hour=11, minute=30, second=0)      #5
    await discord.utils.sleep_until(sleep_time)

#ny_end_loop starter
@NY_end.before_loop
async def wait():
    sleep_time = (datetime.datetime.utcnow() + datetime.timedelta(days=1)).replace(hour=19, minute=30, second=0)      #6
    await discord.utils.sleep_until(sleep_time)




bot.run(os.environ['DISCORD_TOKEN'])


