import discord
from discord.ext import commands

client  = commands.Bot(command_prefix = ".")
@client.command()
async def hello(ctx):
  await ctx.send('Hello There!')

@client.command()
async def ban(ctx, member:discord.Member,*,reason):
  await ctx.send("Member was banned")
  await member.ban(reason=" "+reason)

@client.command()
async def kick(ctx, member:discord.Member,*,reason):
  await ctx.send("Member was kicked")
  await member.kick(reason=" "+reason)



client.run("Your bot's token")
