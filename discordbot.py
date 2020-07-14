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
        
@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/Zippo':
        await message.channel.send('世界で1番可愛い20歳の女の子、じっぽちゃん☆趣味は麻雀、好きな食べ物は酒とタバコ！推してもいいんだからね♡(・ω＜)★')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/じっぽ':
        await message.channel.send('世界で1番可愛い20歳の女の子、じっぽちゃん☆趣味は麻雀、好きな食べ物は酒とタバコ！推してもいいんだからね♡(・ω＜)★')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/usa':
        await message.channel.send('世界一魚臭い男、うさんくさいです。')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/うさ':
        await message.channel.send('世界一魚臭い男、うさんくさいです。')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/io':
        await message.channel.send('私は前に進む、生え際を置き去りにして。はじめまして、私が鯖主のイオです。')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/いお':
        await message.channel.send('私は前に進む、生え際を置き去りにして。はじめまして、私が鯖主のイオです。')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/doku':
        await message.channel.send('MassahRoomの看板娘、鮮血のどくしょです！')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/dokusho':
        await message.channel.send('MassahRoomの看板娘、鮮血のどくしょです！')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/どくしょ':
        await message.channel.send('MassahRoomの看板娘、鮮血のどくしょです！')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/naka':
        await message.channel.send('心はいつも14歳、合法ロリ★なかちゃんです')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/中':
        await message.channel.send('心はいつも14歳、合法ロリ★なかちゃんです')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/kuan':
        await message.channel.send('いつでもボディブローお待ちしています。人間サンドバック34歳、殴りやすいボディのくあんでぇす♪')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/くあん':
        await message.channel.send('いつでもボディブローお待ちしています。人間サンドバック34歳、殴りやすいボディのくあんでぇす♪')

client.run(token)
