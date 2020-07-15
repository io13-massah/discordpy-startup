import discord
from discord.ext import commands
import os
import traceback

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_voice_state_update(member, before, after): 
    if member.guild.id == 724335733841854514 and (before.channel != after.channel):
        alert_channel = client.get_channel(732880477320511551)
        if before.voice.voice_channel is None and after.voice.voice_channel is not None:
        for channel in before.server.channels: 
            msg = f'{member.name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/moni':
        await message.channel.send('もにわぁ〜令和生まれのぴちぴちギャルだよぉ★')
        
client.run(token)
