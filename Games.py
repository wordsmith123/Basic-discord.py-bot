import discord
from discord.ext import commands
import random

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["rps"])
    async def rockpaperscissors(self, ctx, choice=None):
      choices=["rock","paper","scissors"]
      choice=choice.lower()
      if choice in choices:
        bChoice=choices[random.randint(0,2)]
        if bChoice==choice:
          await ctx.send(f"We both chose {choice}!")
        if bChoice+choice in ["rockscissors", "paperrock", "scissorspaper"]:
          await ctx.send(f"I picked {bChoice}! I win!")
        if choice+bChoice in ["rockscissors", "paperrock", "scissorspaper"]:
          await ctx.send(f"I picked {bChoice}. You win.")
      else:
        await ctx.send("That is not a valid choice.")
      
def setup(bot):
    bot.add_cog(Games(bot))