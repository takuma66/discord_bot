from webbrowser import get
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
call_users = set()

class call:
    message = discord.message
    num = 100
    title = "hoge"
    frag = False
    users = set()

    async def respons(self, words):
        self.message = await client.channel.send(words[2]+"をやる人を"+words[1]+"人募集してます!\n参加する人はこのメッセージにリアクションを押してください!")
        self.frag = True
        self.num = words[1]
        self.title = words[2]
    
    async def react_add(self, payload):
        if payload.message_id == self.message:
            user = await client.fetch_user(payload.user_id)
            print(str(user))
            self.users.add(user)
            if len(call_users) == call_num:
                await self.message.reply("締め切りました!")
                self.message = discord.message
                self.frag = False
                self.users = set()
    
    async def react_remove(self, payload):
        if payload.message_id == self.message:
            user = await client.fetch_user(payload.user_id)
            print(str(user))
            self.users.discard(user)
 
            

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

guild_test_server = client.get_guild(995675672443895808)

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
        global call_users
        if payload.message_id == call_message.id:
            user = await client.fetch_user(payload.user_id)
            print(str(user))
            call_users.add(user)
            if len(call_users) == call_num:
                await call_message.reply("締め切りました!")
                call_message = discord.message
                call_frag = False
                call_users = set()


@client.event
async def on_raw_reaction_remove(payload):
    global call_frag
    if call_frag:
        global call_message 
        global call_users
        user = await client.fetch_user(payload.user_id)
        call_users.discard(user)


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)