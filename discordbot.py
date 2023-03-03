import discord
from discord.ext import commands
import random
from call import Call
from send_content import Content

TOKEN = 'paste Bot Token here'

# 接続に必要なオブジェクトを生成
bot = commands.Bot(activity=discord.Game(name='喫茶ステラと死神の蝶'), command_prefix='/')

c = Call()

content = Content()

@bot.event
async def on_ready():
    print('ログインしました')
    print('------')

@bot.command()
async def map(ctx):
    await ctx.send(random.choice(content.get_maps()))

@bot.command()
async def coin(ctx):
    await ctx.send(random.choice(content.get_cointoss()))

@bot.command()
async def call(ctx, num: int, title: str):
    await c.respons(ctx, num, title)

@bot.event
async def on_raw_reaction_add(payload):
    await c.react_add(payload, bot)

@bot.event
async def on_raw_reaction_remove(payload):
    await c.react_remove(payload, bot)


bot.run(TOKEN)

'''
# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    words = message.content.split(" ")
    if words[0] == "/map":
        content = random.choice(random_maps)
        await message.channel.send(content)
    elif words[0] == "/coin":
        content = random.choice(cointoss)
        await message.channel.send(content)
    elif words[0] == "/call":
        c.print_attribute()
        await c.respons(words, message)
        c.print_attribute()

@client.event
async def on_raw_reaction_add(payload):
    c.print_attribute()
    if c.frag:
        await c.react_add(payload)

@client.event
async def on_raw_reaction_remove(payload):
    if c.flag:
        await c.react_remove(payload)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
'''  
