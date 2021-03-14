import discord
from discord.ext import commands

client  = commands.Bot(command_prefix = ".")
@client.command()
async def hello(ctx):
  await ctx.send('Hello There!')
  
#INSERT BOT'S TOKEN
client.run('Nice try, but insert your bot's token over HERE!!!!')
