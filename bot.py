import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random



load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
#intents.message_content = True



bot = commands.Bot(command_prefix="$", intents = intents)

@bot.event
async def on_ready():
    print("Bot wurde erfolgreich hochgefahren")

@bot.command(brief = "Sends a Picture of a random Silly Cat!")
async def sillyCat(message):
    cats = []
    for file_path in os.listdir("SillyCats"):
        if os.path.isfile(os.path.join("SillyCats", file_path)):
            cats.append("SillyCats/" + file_path)
    randomIndex = random.randint(0, len(cats) - 1)
    fileToSend = str(cats[randomIndex])

    await message.channel.send(file=discord.File(fileToSend))

    print(cats)

bot.run(TOKEN)