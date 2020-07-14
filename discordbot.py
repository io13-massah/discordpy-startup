import discord
from discord.ext import commands
import os
import traceback

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
bot = commands.Bot(command_prefix='/')

@client.event
async def on_voice_state_update(member, before, after): 
    if member.guild.id == 724335733841854514 and (before.channel != after.channel):
        alert_channel = client.get_channel(726315919093137458)
        if before.channel is None: 
            msg = f'@イオーナー {member.name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)

@bot.command()
async def moni(ctx):
    await ctx.send('もにわぁ〜令和生まれのぴちぴちギャルだよぉ★')

client.run(token)
bot.run(token)
