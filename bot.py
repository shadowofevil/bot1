import sys
import discord
from discord.ext import commands 

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">>bot is online <<")

@bot.event
async def on_member_join(memeber):
    channel=bot.get_channel(733714161867161623)
    await channel.send(f'{memeber} join!')

@bot.event
async def on_member_remove(memeber):
    channel=bot.get_channel(733714161867161623)
    await channel.send(f'{memeber} leave!')

@bot.group()
async def b(self):
    pass

@b.command()
async def a(self):
    #self.ctx=ctx
    channel=bot.get_channel(733714161867161623)
    role.mention='@參戰人員'
    await channel.send(f'{role} 1王 ')

@b.command()
async def c(self):
   #self.ctx=ctx
   channel=bot.get_channel(733714161867161623)
   await channel.send('@參戰人員 2王 ')

bot.run('NzMzNzAzMTA2NjQ2MjQ1NDI3.XxHARA.UDqhsntV1Zz7H8l2DCG9Bowb3PI')