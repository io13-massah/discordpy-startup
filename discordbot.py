import discord
from discord.ext import commands
import os
import traceback

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_voice_state_update(member, before, after): 
    if member.guild.id == 724335733841854514 and (before.channel != after.channel):
        alert_channel = client.get_channel(726315919093137458)
        if before.channel is None: 
            msg = f'{member.name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/moni':
        await message.channel.send('もにわぁ〜令和生まれのぴちぴちギャルだよぉ★')
        
@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/zippo':
        await message.channel.send('世界で1番可愛い20歳の女の子、じっぽちゃん☆趣味は麻雀、好きな食べ物は酒とタバコ！推してもいいんだからね♡(・ω＜)★')
        
client.run(token)
