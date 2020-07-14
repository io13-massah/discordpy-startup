from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == 724335733841854514 and (before.channel != after.channel):
        alert_channel = client.get_channel(726315919093137458)
        if before.channel is None:
            msg = f'@ボイチャ通知OK {member.name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def moni(ctx):
    await ctx.send('もにわぁ〜令和生まれのぴちぴちギャルだよぉ★')

@bot.command()
async def zippo(ctx):
    await ctx.send('世界で1番可愛い20歳の女の子、じっぽちゃん☆趣味は麻雀、好きな食べ物は酒とタバコ！推してもいいんだからね♡(・ω＜)★')

@bot.command()
async def じっぽ(ctx):
    await ctx.send('世界で1番可愛い20歳の女の子、じっぽちゃん☆趣味は麻雀、好きな食べ物は酒とタバコ！推してもいいんだからね♡(・ω＜)★')

@bot.command()
async def Zippo(ctx):
    await ctx.send('世界で1番可愛い20歳の女の子、じっぽちゃん☆趣味は麻雀、好きな食べ物は酒とタバコ！推してもいいんだからね♡(・ω＜)★')

@bot.command()
async def usa(ctx):
    await ctx.send('世界一魚臭い男、うさんくさいです。')

@bot.command()
async def うさ(ctx):
    await ctx.send('世界一魚臭い男、うさんくさいです。')

@bot.command()
async def io(ctx):
    await ctx.send('私は前に進む、生え際を置き去りにして。はじめまして、私が鯖主のイオです。')

@bot.command()
async def doku(ctx):
    await ctx.send('MassahRoomの看板娘、鮮血のどくしょです！')

@bot.command()
async def どくしょ(ctx):
    await ctx.send('MassahRoomの看板娘、閃光のどくしょです！')

@bot.command()
async def dokusho(ctx):
    await ctx.send('MassahRoomの看板娘、どくしょです！')

@bot.command()
async def naka(ctx):
    await ctx.send('心はいつも14歳、合法ロリ★なかちゃんです')

@bot.command()
async def 中(ctx):
    await ctx.send('心はいつも14歳、合法ロリ★なかちゃんです')

@bot.command()
async def くあん(ctx):
    await ctx.send('いつでもボディブローお待ちしています。人間サンドバック34歳、殴りやすいボディのたくあんでぇす♪')

@bot.command()
async def kuan(ctx):
    await ctx.send('いつでもボディブローお待ちしています。人間サンドバック34歳、殴りやすいボディのたくあんでぇす♪')

@bot.command()
async def たくあん(ctx):
    await ctx.send('いつでもボディブローお待ちしています。人間サンドバック34歳、殴りやすいボディのたくあんでぇす♪')

@bot.command()
async def 悪人(ctx):
    await ctx.send('いつでもボディブローお待ちしています。人間サンドバック34歳、殴りやすいボディのたくあんでぇす♪')

bot.run(token)
