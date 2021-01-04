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
P_ROOM=int(774275081223274536)

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
  
# @client.event
# async def on_member_join(member): #member入場時
#   channel = client.get_channel(ID_IN_ROOM)
#   await channel.send("get channel ID")
#   await channel.send("event:member join")
#   user = client.get_user(member.id)
#   await channel.send("get memberID")
#   server=client.get_guild(ServerID)
#   await channel.send("get severID")
#   B_invite_B=0;C_invite_C=0;D_invite_D=0;E_invite_E=0;F_invite_F=0;
#   Linvite=await server.invites()
#   await channel.send("invites ok")
#   for item in Linvite :
#     if "AvBCBEp" in str(item) :
#         C_invite_C=item.uses
#     elif "XYSSEyF" in str(item) :
#         B_invite_B=item.uses
#     elif "8TUtXWN" in str(item) :
#         D_invite_D=item.uses
#     elif "VRu4htG" in str(item) :
#         E_invite_E=item.uses
#     elif "5ptBtvf" in str(item) :
#         F_invite_F=item.uses
#   await channel.send("input integer")
#   txt1=str(user.name)+"#"+str(user.discriminator)
#   txt2=str(B_invite_B)+"."+str(C_invite_C)+"."+str(D_invite_D)+"."+str(E_invite_E)+"."+str(F_invite_F)
#   await channel.send(txt1)
#   await channel.send(txt2)
#   return
  
  
#clear
@client.event
async def on_message(message): #message受信時
  global bump_flag
  if message.author.bot: #Botだった場合は反応しない
    return

  if message.channel.id == ID_BUMP_ROOM and message.content == "!d bump": #disboardのbumpコマンド実行時&チャンネル指定
    if bump_flag == 1:
      bump_flag = 0
      bumper_message="fastest bumper : "+"<@!"+str(message.author.id)+">"
      await message.channel.send(bumper_message)
      await asyncio.sleep(7200)   #2時間待つ
      bump_flag = 1
      await message.channel.send("<@&724619422769348671> <@&765198359014277121> remind 2 hours") #remind bump用ロール
    else:
      miss_message="<@!"+str(message.author.id)+"> "+"LOSE"
      await message.channel.send(miss_message) #error message
      await message.channel.send("なんで負けたか 次のbumpまでに考えといてください。")

  if message.channel.id == ID_SELF_MEN or message.channel.id == ID_SELF_WOMEN: #自己紹介(男or女)のチャンネル
    member = message.channel.guild.get_member(message.author.id)
    role = message.guild.get_role(SELF_ROLE_ID)
    await member.add_roles(role) #自己紹介済みのロールID
    if message.channel.id == ID_SELF_MEN:
      role = message.guild.get_role(M_ROLE_ID)
      await member.add_roles(role) #m
    else:
      role = message.guild.get_role(F_ROLE_ID)
      await member.add_roles(role) #f

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
  else:
    if not nvwau:
      await after.add_roles(role) #vwauのロールID

@client.event
async def on_error(event,args,kwargs): #Error時ハンドラ
  channel = client.get_channel(P_ROOM)
  await channel.send("on_error")
  await channel.send(event)
  await channel.send(args)
#   await channel.send(kwargs)
  await channel.send(sys.exc_info())
  
# @client.event
# async def on_socket_raw_receive(msg): 
#   channel = client.get_channel(P_ROOM)
#   await channel.send("on_socket_raw_receive")
#   await channel.send(msg)
#   return
    
# do not use
# @client.event
# async def on_socket_raw_send(payload): 
#   channel = client.get_channel(P_ROOM)
#   await channel.send("on_socket_raw_send")
#   await channel.send(payload)
  
@client.event
async def on_bulk_message_delete(messages): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_bulk_message_delete")
  await channel.send(messages)
  
# @client.event
# async def on_raw_message_delete(payload): 
#   channel = client.get_channel(P_ROOM)
#   await channel.send("on_raw_message_delete")
#   await channel.send(payload)
#   return
  
@client.event
async def on_raw_bulk_message_delete(payload): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_raw_bulk_message_delete")
  await channel.send(payload)
  
# @client.event
# async def on_message_edit(before, after): 
#   channel = client.get_channel(P_ROOM)
#   await channel.send("on_message_edit")
#   await channel.send(before)
#   await channel.send(after)
#   return
  
# @client.event
# async def on_raw_message_edit(payload): 
#   channel = client.get_channel(P_ROOM)
#   await channel.send("on_raw_message_edit")
#   await channel.send(payload)
#   return
  
# @client.event
# async def on_reaction_add(reaction, user): 
#   channel = client.get_channel(P_ROOM)
#   await channel.send("on_reaction_add")
#   await channel.send(reaction)
#   await channel.send(user)
#   return

# @client.event
# async def on_raw_reaction_add(payload): 
#   channel = client.get_channel(P_ROOM)
#   await channel.send("on_raw_reaction_add")
#   await channel.send(payload)
#   return

# @client.event
# async def on_reaction_remove(reaction, user): 
#   channel = client.get_channel(P_ROOM)
#   await channel.send("on_reaction_remove")
#   await channel.send(reaction)
#   await channel.send(user)

# @client.event
# async def on_raw_reaction_remove(payload): 
#   channel = client.get_channel(P_ROOM)
#   await channel.send("on_raw_reaction_remove")
#   await channel.send(payload)

@client.event
async def on_reaction_clear(message, reactions): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_reaction_clear")
  await channel.send(message)
  await channel.send(reactions)

@client.event
async def on_raw_reaction_clear(payload): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_raw_reaction_clear")
  await channel.send(payload)

@client.event
async def on_reaction_clear_emoji(reaction): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_reaction_clear_emoji")
  await channel.send(reaction)

@client.event
async def on_raw_reaction_clear_emoji(payload): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_raw_reaction_clear_emoji")
  await channel.send(payload)

@client.event
async def on_private_channel_create(channel): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_private_channel_create")
  await channel.send(channel)

@client.event
async def on_private_channel_delete(channel): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_private_channel_delete")
  await channel.send(channel)

@client.event
async def on_private_channel_update(before, after): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_private_channel_update")
  await channel.send(before)
  await channel.send(after)

@client.event
async def on_private_channel_pins_update(channel, last_pin): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_private_channel_pins_update")
  await channel.send(channel)
  await channel.send(last_pin)

# @client.event
# async def on_guild_channel_create(channel): 
#   channel = client.get_channel(P_ROOM)
#   await channel.send("on_guild_channel_create")
#   await channel.send(channel)

# @client.event
# async def on_guild_channel_update(before, after): 
#   channel = client.get_channel(P_ROOM)
#   await channel.send("on_guild_channel_update")
#   await channel.send(before)
#   await channel.send(after)
#   return

@client.event
async def on_guild_channel_pins_update(channel, last_pin): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_guild_channel_pins_update")
  await channel.send(channel)
  await channel.send(last_pin)

# @client.event
# async def on_guild_channel_delete(channel): 
#   channel = client.get_channel(P_ROOM)
#   await channel.send("on_guild_channel_delete")
#   await channel.send(channel)

@client.event
async def on_webhooks_update(channel): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_webhooks_update")
  await channel.send(channel)

@client.event
async def on_member_remove(member): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_member_remove")
  await channel.send(member)

@client.event
async def on_user_update(before, after): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_user_update")
  await channel.send(before)
  await channel.send(after)

@client.event
async def on_guild_join(guild): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_guild_join")
  await channel.send(guild)

@client.event
async def on_guild_remove(guild): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_guild_remove")
  await channel.send(guild)

@client.event
async def on_guild_update(before, after): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_guild_update")
  await channel.send(before)
  await channel.send(after)

# @client.event
# async def on_guild_role_create(role): 
#   channel = client.get_channel(P_ROOM)
#   await channel.send("on_guild_role_create")
#   await channel.send(role)

# @client.event
# async def on_guild_role_delete(role): 
#   channel = client.get_channel(P_ROOM)
#   await channel.send("on_guild_role_delete")
#   await channel.send(role)

# @client.event
# async def on_guild_role_update(before, after): 
#   channel = client.get_channel(P_ROOM)
#   await channel.send("on_guild_role_update")
#   await channel.send(before)
#   await channel.send(after)
#   return

# @client.event
# async def on_guild_available(guild): 
#   channel = client.get_channel(P_ROOM)
#   await channel.send("on_guild_available")
#   await channel.send(guild)
#   return

@client.event
async def on_guild_unavailable(guild): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_guild_unavailable")
  await channel.send(guild)

# @client.event
# async def on_member_ban(guild, user): 
#   channel = client.get_channel(P_ROOM)
#   await channel.send("on_member_ban")
#   await channel.send(guild)
#   await channel.send(user)
#   return

@client.event
async def on_invite_create(invite): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_invite_create")
  await channel.send(invite)

@client.event
async def on_invite_delete(invite): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_invite_delete")
  await channel.send(invite)

@client.event
async def on_member_join(member): 
  channel = client.get_channel(P_ROOM)
  await channel.send("on_member_join")
  await channel.send(member)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
