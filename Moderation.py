import discord
from discord.ext import commands

class Moderation(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, user : discord.Member):
    if ctx.author == user:
      await ctx.send("You cannot kick yourself.")
    if ctx.author.top_role.position >= user.top_role.position:
      await user.kick()
      embed = discord.Embed(title=f'User {user.name} has been kicked.', color=0x00ff00)
    else:
      embed=discord.Embed(title="Error: User role above author's top role", color=0x00ff00)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)


  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def ban(self, ctx, user : discord.Member):
    if ctx.author == user:
      embed=discord.Embed(title="Error: Target is author.",color=0x00ff00)
    elif ctx.author.top_role.position >= user.top_role.position:
      await user.ban()
      embed = discord.Embed(title=f'User {user.name} has been banned.', color=0x00ff00)    
    else:
      embed=discord.Embed(title="Error: Target's top role above author's top role", color=0x00ff00)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def prune(self, ctx, count: int):
    if count>100:
        count = 100
    await ctx.message.channel.purge(limit=count, bulk=True)
    embed=discord.Embed(title="Purge completed")
    embed.add_field(name="Messages deleted:", value=count)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embed, delete_after=10)

def setup(bot):
    bot.add_cog(Moderation(bot))