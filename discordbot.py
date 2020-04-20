# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzAxNjg3NTQ3OTMxMzk0MTQ5.Xp1JEA.0pYjCMHXw31Ea8snGUDWfw5bQAI'

# 接続に必要なオブジェクトを生成
client = discord.Client()




# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')


@client.event
async def on_message(message):
    if message.content == '/touban'

        await message.channel.send(author.role.name)

@client.event
async def on_message(message):

    if message.content == '/omikuji'
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author
            import random
            omikuji = [
                "大吉"   if i < 2 else
                "中吉"   if 2 <= i < 10 else
                "小吉"   if 10 <= i < 20 else
                "吉"     if 20 <= i < 40 else
                "末吉"   if 40 <= i < 50 else
                "凶"     if 50 <= i < 55 else
                "中凶"   if 55 <= i < 59 else
                "大凶"   for i in range(61)]

                print(message.author.name+"さんの運勢は"+omikuji[random.randrange(len(omikuji))]+"です。")

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
