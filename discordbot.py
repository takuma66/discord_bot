import discord
import random

TOKEN = 'OTk2NDAzNzkwMzE4MTQ5NzEy.Gp6YKa.1-ImE1QEmdqCXra6VaKlLT9hwG9rYnJBQe-jps' # TOKENを貼り付け

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 他の関数内で呼び出すためのグローバル変数
# 関数内で使うときは `global [変数名]`で定義
call_message = discord.message # 空のmessageインスタンスで初期化 
call_num = 100
call_title = "hoge"
cnt = 0
call_frag = False # Trueのとき、callコマンドで募集中

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

    words = message.content.split(" ")
    if words[0] == "/map":
        content = random.choice(random_maps)
        await message.channel.send(content)
    elif words[0] == "/coin":
        content = random.choice(cointoss)
        await message.channel.send(content)
    elif words[0] == "/call":
        global call_message 
        global call_num
        global call_title
        global call_frag
        call_num = int(words[1])
        title = words[2]
        print(call_num)
        print(title)
        call_message = await message.channel.send(words[2]+"をやる人を"+words[1]+"人募集してます!\n参加する人はこのメッセージにリアクションを押してください!")
        call_frag = True
        


@client.event
async def on_raw_reaction_add(payload):
    global call_frag
    if call_frag:
        global call_message 
        global call_num
        global call_title
        if payload.message_id == call_message.id:
            react_users = set()
            react_users.add(payload.user_id)
            if len(react_users) == call_num:
                await call_message.reply("締め切りました!")
                call_message = discord.message
                call_frag = False

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)