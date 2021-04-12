import discord
from discord.ext import commands

class Utility(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.command()
  async def botinvite(self, ctx):
    embed=discord.Embed(title=f"Invite {self.bot.user.name} to your server!", description=f"Click [here](    https://discord.com/oauth2/authorize?client_id={self.bot.user.id}&scope=bot&permissions=93190)")
    await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Utility(bot))