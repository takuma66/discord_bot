import discord
# ゲーム参加者の募集を管理するクラスcall
class Call:
    message = discord.message
    num = 100
    title = "hoge"
    frag = False
    users = set()

    # メンバ変数を確認するためのデバッガプリンタ
    def print_attribute(self):
        print(self.num)
        print(self.title)
        if self.frag:
            print("True")
        else:
            print("False")

    # 募集がかかったときの応答
    # words[]はwords[0]に"/call",words[1]に募集人数、words[2]にタイトルを記入
    async def respons(self, ctx, num, title):
        self.frag = bool(True)
        self.num = int(num)
        self.title = str(title)
        self.message = await ctx.send(self.title+"をやる人を"+str(num)+"人募集してます!\n参加する人はこのメッセージにリアクションを押してください!")
    
    # リアクション数を数え、募集人数に達したら締め切る
    async def react_add(self, payload, bot):
        if payload.message_id == self.message.id:
            user = await bot.fetch_user(payload.user_id)
            print("add: " + str(user))
            self.users.add(user)
            if self.num == len(self.users):
                await self.message.reply("締め切りました!")
                self.message = discord.message
                self.frag = bool(False)
                self.users = set()
    
    # リアクションを消した人を数える
    async def react_remove(self, payload, bot):
        if payload.message_id == self.message.id:
            user = await bot.fetch_user(payload.user_id)
            print("remove: " + str(user))
            self.users.discard(user)