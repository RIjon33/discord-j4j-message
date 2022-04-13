import discord
from discord.ext import commands, tasks
import random
import asyncio
import datetime


min_age = '14' # minimum account age when doing j4j
response_delay = random.randint(3,8) # delay after responding when someone DMs you
done_delay = random.randint(15,20) # delay between saying your done message after sending your message
msg_delay = random.randint(30,60) # delay between sending j4j messages to servers

done_msg = [
'done',
'dn',
'I joined'
] # message sent after you send your response msg
j4j_msg = [
'j4j',
'j4j fast',
'join 4 join',
'j4j dm fast',
'j4j fast',
'j4j NO BOTS',
'j4j no bots pls',
'j4j old accounts only',
'j4j dm',
'J4J'
] # message sent to server's j4j channels
dm_msg = [
'j4j',
'j4j first u',
'j4j'
] # first message sent when you do j4j with someone

link = '' # server invite link 
token = '' # your token

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!',self_bot=True)
ready = False

@bot.event
async def on_ready():
    print(f"Starting bot as {bot.user}")


@tasks.loop(seconds=msg_delay)
async def j4j():
    for guild in bot.guilds:
        for channel in guild.channels:
            if 'j4j' in channel.name:
                channel = bot.get_channel(channel.id)
                try:
                    await channel.send(random.choice(j4j_msg))
                    print(f"> Sent message in {channel.name} in {guild.name}")
                except:
                    print(f"> Couldn't send message in {channel} in {guild.name}")
@j4j.before_loop
async def before_j4j():
  await bot.wait_until_ready()
j4j.start()


bot.run(token, bot=False)


## MADE BY RIjon33