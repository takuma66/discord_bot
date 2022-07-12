import discord
import random

TOKEN = 'OTk2NDAzNzkwMzE4MTQ5NzEy.Gp6YKa.1-ImE1QEmdqCXra6VaKlLT9hwG9rYnJBQe-jps' # TOKENを貼り付け

# 接続に必要なオブジェクトを生成
client = discord.Client()

random_maps = [
    "アセント",
    "スプリット",
    "ヘイブン",
    "バインド",
    "アイスボックス",
    "ブリーズ",
    "フラクチャー",
    "パール"
]

cointoss = [
    "表",
    "裏"
]

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

    if message.content == "/map":
        content = random.choice(random_maps)
        await message.channel.send(content)
    elif message.content == "/coin":
        content = random.choice(cointoss)
        await message.channel.send(content)
    elif message.content == "/team":
        channel = client.get_channel(960527660327505930)
        member = channel.members
        random.shuffle(member)
        harf = int(len(member)/2)
        team = member[:harf]
        for mem in team:
            await message.channel.send(mem.display_name)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)