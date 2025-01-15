import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())



# //////////////////// Bot Event /////////////////////////
# คำสั่ง bot พร้อมใช้งานแล้ว
@bot.event
async def on_ready():
    print("Bot Online!")
    print("555")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")



# คำสั่ง chatbot
@bot.event
async def on_message(message):
    mes = message.content # ดึงข้อความที่ถูกส่งมา
    if mes == 'bot':
        await message.channel.send("มีเหี้ยไร") # ส่งกลับไปที่ห้องนั่น

    elif mes == 'hi bot':
        await message.channel.send("แหมมาพิมพ์อินเตอร์ดูก็รู้ว่า เป็นคนไทย คนที่เป็นเกย์นั่นก็คือ, " + str(message.author.name))

    await bot.process_commands(message)
    # ทำคำสั่ง event แล้วไปทำคำสั่ง bot command ต่อ




# ///////////////////// Commands /////////////////////
# กำหนดคำสั่งให้บอท

@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author.name}!")


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


# Slash Commands
@bot.tree.command(name='hellobot', description='Replies with Hello')
async def hellocommand(interaction):
    await interaction.response.send_message("Hello It's me BOT DISCORD")


@bot.tree.command(name='name')
@app_commands.describe(name = "What's your name?")
async def namecommand(interaction, name : str):
    await interaction.response.send_message(f"สวัสดีคุณ{name}เป็นเกย์หรือเปล่า")


# Embeds

@bot.tree.command(name='dddd', description='Bot Commands')
async def helpcommand(interaction):
    emmbed = discord.Embed(title='...',
                           description='ผู้สร้างทั้งหมดjo',
                           color=0x66FFFF,
                           timestamp= discord.utils.utcnow())


    # ใส่ข้อมูล
    emmbed.add_field(name='ig ผู้สร้าง1', url='https://www.instagram.com/adc_108/', inline=True)
    emmbed.add_field(name='ig ผู้สร้าง2', url='https://www.instagram.com/atkxncry_x016/', inline=True)
   
    emmbed.set_author(name='discord', url='https://discord.gg/eFVs3KWG', icon_url='https://media.discordapp.net/attachments/1078962950691373117/1174118238733480026/image0.gif?ex=6788e392&is=67879212&hm=6b81c55686ff66496370dd78235657ac6ecf59428ade3a954378131572b7e3d3&')

    # ใส่รูปเล็ก-ใหญ่
    emmbed.set_thumbnail(url='https://media.discordapp.net/attachments/1078962950691373117/1174118238733480026/image0.gif?ex=6788e392&is=67879212&hm=6b81c55686ff66496370dd78235657ac6ecf59428ade3a954378131572b7e3d3&')
    emmbed.set_image(url='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdG5heHRlcXEyZHlvOHUxN3R1eDIxdXQ1cjdqenZyaXMzd3IyMXh0eCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/CkzASXWphfkQ5CF6ny/giphy.gif')

    # Footer เนื้อหาส่วนท้าย
    emmbed.set_footer(text='Footer', icon_url='https://media.discordapp.net/attachments/1078962950691373117/1174118238733480026/image0.gif?ex=6788e392&is=67879212&hm=6b81c55686ff66496370dd78235657ac6ecf59428ade3a954378131572b7e3d3&')

    await interaction.response.send_message(embed = emmbed)




server_on()

bot.run(os.getenv('TOKEN'))
