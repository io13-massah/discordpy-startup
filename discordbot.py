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
        if before.channel is None and after.channel is not None:
            msg = f'{member.name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)
        
client.run(token)
