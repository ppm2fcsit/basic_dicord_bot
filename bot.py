import os #จัดการข้อมูล
import discord #discord API
import random
from dotenv import load_dotenv #การจัดข้อมูล

load_dotenv()

#Set information
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event #decoretion ตกแต่ง method/function 
async def on_ready(): # ฟังก์ชั่นการยืนยันการเชื่อมต่อ python และ Discord 
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        #print(guild.name)
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    messageChoice = [
        'I\'m the human form of the 💯 emoji.', 
        'Bingpot!',
        'Cool. Cool cool cool cool cool cool cool, no doubt no doubt no doubt no doubt.'
        ]
    if message.content == '99!':
        response = random.choice(messageChoice) #random.choice => การสุ่มข้อมูลใน list [z,z,x]
        await message.channel.send(response)
    
    if message.content == 'hello':
        response = "Hi"
        await message.channel.send(response)

client.run(TOKEN) #การเริ่มการเชื่อมต่อ Discord API