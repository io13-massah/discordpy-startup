# インストールした discord.py を読み込む
import discord
import os
import asyncio
import time

# アクセストークン(Botの)
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

#serverID
ServerID=int(724335733841854514)

#ChannnelID List
ID_SELF_MEN=int(738589598887837817)
ID_SELF_WOMEN=int(738589663937429585)
ID_BUMP_ROOM=int(726320618613637132)
ID_IN_ROOM=int(730798230702522400)
ID_START_ROOM=int(751583201314472076)

#RoleID List
SELF_ROLE_ID=int(738608018383700008)
M_ROLE_ID=int(739714926158938132)
F_ROLE_ID=int(734362306426961951)
FR_ROLE_ID=int(738942097519804506)
VWAU_ROLE_ID=int(731387113068691506)
NVWAU_ROLE_ID=int(735786611073351720)

#flagment
bump_flag=1

#clear
@client.event
async def on_ready(): #Bot起動準備完了時
  channel = client.get_channel(ID_START_ROOM)
  await channel.send("Ready")

#clear
@client.event
async def on_member_join(member):
  channel = client.get_channel(ID_IN_ROOM)
  await channel.send("get channel ID")
  await channel.send("event:member join")
  user = client.get_user(member.id)
  await channel.send("get memberID")
  server=client.get_guild(ServerID)
  await channel.send("get severID")
  B_invite_B=0;C_invite_C=0;D_invite_D=0;E_invite_E=0;F_invite_F=0;
  Linvite=await server.invites()
  await channel.send("invites ok")
  for item in Linvite :
    if "AvBCBEp" in str(item) :
        C_invite_C=item.uses
    elif "XYSSEyF" in str(item) :
        B_invite_B=item.uses
    elif "8TUtXWN" in str(item) :
        D_invite_D=item.uses
    elif "VRu4htG" in str(item) :
        E_invite_E=item.uses
    elif "5ptBtvf" in str(item) :
        F_invite_F=item.uses
  await channel.send("input integer")
  txt1=str(user.name)+"#"+str(user.discriminator)
  txt2=str(B_invite_B)+"."+str(C_invite_C)+"."+str(D_invite_D)+"."+str(E_invite_E)+"."+str(F_invite_F)
  await channel.send(txt1)
  await channel.send(txt2)

#clear
@client.event
async def on_message(message): #message受信時
  global bump_flag
  if message.author.bot: #Botだった場合は反応しない
    return

  if message.channel.id == ID_BUMP_ROOM and message.content == "bump": #disboardのbumpコマンド実行時&チャンネル指定
    if bump_flag == 1:
      bump_flag = 0
      await message.channel.send("fastest bumper:<@!message.author.id>")
      await asyncio.sleep(7200)   #2時間待つ
      bump_flag = 1
      await message.channel.send("<@&724619422769348671> <@&765198359014277121> remind 2 hours") #remind bump用ロール
      return
    else:
      await message.channel.send("Bumped within 2 hours") #error message

  if message.channel.id == ID_SELF_MEN or message.channel.id == ID_SELF_WOMEN: #自己紹介(男or女)のチャンネル
    member = message.channel.guild.get_member(message.author.id)
    role = message.guild.get_role(SELF_ROLE_ID)
    await member.add_roles(role) #自己紹介済みのロールID
    if message.channel.id == ID_SELF_MEN:
      role = message.guild.get_role(M_ROLE_ID)
      await member.add_roles(role) #m
      return member
    else:
      role = message.guild.get_role(F_ROLE_ID)
      await member.add_roles(role) #f
      return member

#clear
@client.event
async def on_member_update(before, after):#Member情報変更時に呼び出し
  if before.roles == after.roles: #更新前と更新後のロールが同じ
    return
  
  vwau=False;nvwau=False
  
  for item in after.roles :
    if str(item)=='vwau' :
        vwau = True
        #該当する要素が見つかった時点でブレイク。
        break
  for item in after.roles :
    if str(item)=='nvwau' :
        nvwau = True
        #該当する要素が見つかった時点でブレイク。
        break
  
  role = after.guild.get_role(NVWAU_ROLE_ID)
  if vwau:
    if nvwau:
      await after.remove_roles(role) #vwauのロールID
      return after
  else:
    if not nvwau:
      await after.add_roles(role) #vwauのロールID
      return after

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
