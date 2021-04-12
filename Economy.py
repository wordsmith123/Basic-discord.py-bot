import discord
from discord.ext import commands
import sqlite3
import random

class Economy(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(aliases=["start"])
  async def register(self, ctx):
    con=sqlite3.connect("accs.db")
    cur=con.cursor()
    account=cur.execute(f"SELECT * FROM Accounts WHERE id = {ctx.author.id}").fetchone()
    if account == None:
      cur.execute(f"INSERT INTO Accounts VALUES({ctx.author.id}, 0, 0)")
      con.commit()
      await ctx.reply("Account made!")
    else:
      await ctx.reply("You already have an account.")
    con.close()

  @commands.command(aliases=["bal"])
  async def balance(self, ctx, user: discord.Member=None):
    if user == None:
      user=ctx.author
    con=sqlite3.connect("accs.db")
    cur=con.cursor()
    account=cur.execute(f"SELECT * FROM Accounts WHERE id = {user.id}").fetchone()
    con.close()
    if account == None:
      await ctx.send(f"{user.mention} doesn't have an account.")
    else:
      em=discord.Embed(color=user.color, title=f"{ctx.author.name}'s balance")
      em.add_field(name="Wallet:", value=account[1])
      em.add_field(name="Bank:", value=account[2]) 
      await ctx.send(embed=em) 

  @commands.command()
  async def beg(self, ctx):
    con=sqlite3.connect("accs.db")
    cur=con.cursor()
    account=cur.execute(f"SELECT * FROM Accounts WHERE id = {ctx.author.id}").fetchone()
    if account == None:
      await ctx.reply("You don't have an account.")
    else:
      amount=random.randint(30,100)
      cur.execute(f"UPDATE Accounts SET wallet = {account[1]+amount} WHERE id = {ctx.author.id}")
      con.commit()
      await ctx.reply(f"You were given ${amount}.")
    con.close()
  
  @commands.command(aliases=["dep"])
  async def deposit(self, ctx, amount: int):
    con=sqlite3.connect("accs.db")
    cur=con.cursor()
    account=cur.execute(f"SELECT * FROM Accounts WHERE id = {ctx.author.id}").fetchone()
    if account == None:
      await ctx.reply("You don't have an account.")
    elif amount>account[1]:
      await ctx.reply("You cannot deposit more than you have.")
    elif 0>amount:
      await ctx.reply("You cannot deposit a negative amount.")
    else:
      cur.execute(f"UPDATE Accounts SET wallet = {account[1]-amount}, bank = {account[2]+amount} WHERE id = {ctx.author.id}")
      con.commit()
      await ctx.reply(f"You deposited ${amount}.")
    con.close()

  @commands.command(aliases=["with"])
  async def withdraw(self, ctx, amount: int):
    con=sqlite3.connect("accs.db")
    cur=con.cursor()
    account=cur.execute(f"SELECT * FROM Accounts WHERE id = {ctx.author.id}").fetchone()
    if account == None:
      await ctx.reply("You don't have an account.")
    elif amount>account[2]:
      await ctx.reply("You cannot withdraw more than you have in your bank.")
    elif 0>amount:
      await ctx.reply("You cannot withdraw a negative amount.")
    else:
      cur.execute(f"UPDATE Accounts SET wallet = {account[1]+amount}, bank = {account[2]-amount} WHERE id = {ctx.author.id}")
      con.commit()
      await ctx.reply(f"You withdrew ${amount}.")
    con.close()

def setup(bot):
    bot.add_cog(Economy(bot))