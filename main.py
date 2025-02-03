import discord
from bot_mantik import gen_pass

# İstekler değişkeni botun yetkilerini saklar
intents = discord.Intents.default()
# Mesaj okuma yetkisini etkinleştirme
intents.message_content = True
# Bir bot oluşturma ve yetkileri aktarma
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yapıldı')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Merhaba!")
    elif message.content.startswith('$görüşürüz'):
        await message.channel.send("Görüşürüz")
    elif message.content.startswith('$naber'):
        await message.channel.send("İyiyim sen?")
    elif message.content.startswith('$iyiyim sağol'):
        await message.channel.send("Harikaaa!")
    elif message.content.startswith('$5x5 kaç eder?'):
        await message.channel.send("25")
    elif message.content.startswith('$doğru'):
        await message.channel.send("Oleeeeey!")
    elif message.content.startswith('$tebrikler'):
        await message.channel.send("Sağol!")
    elif message.content.startswith('Ben kaçar'):
        await message.channel.send("Tamam.")
    elif message.content.startswith('$baybay'):
        await message.channel.send("Görüşürüz!")
    else:
        await message.channel.send("Şifreniz: " + gen_pass(50))

client.run("TOKENİNİZİ GİRİN")
