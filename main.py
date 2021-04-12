import os #Used for token
import discord
from discord.ext import commands
import sqlite3 #Used for economy database
con=sqlite3.connect("accs.db")
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Accounts (Id INT PRIMARY KEY, Wallet INT DEFAULT 0, Bank INT DEFAULT 0)")
con.commit()
con.close()
token=os.getenv("TOKEN")

intents=discord.Intents.default()
intents.members=True
bot=commands.Bot(command_prefix="<", intents=intents)

bot.load_extension("Economy")
bot.load_extension("Games")
bot.load_extension("Moderation")
bot.load_extension("Utility")

@bot.event
async def on_ready():
  print("On!")

bot.run(token)