import discord
from discord.ext import commands

client  = commands.Bot(command_prefix = ".")
@client.command()
async def hello(ctx):
  await ctx.send('Hello There!')
#---------MODERATON COMMANDS--------------
@client.command()
async def ban(ctx, member:discord.Member,*,reason):
  await ctx.send("Member was banned")
  await member.ban(reason=" "+reason)

@client.command()
async def kick(ctx, member:discord.Member,*,reason):
  await ctx.send("Member was kicked")
  await member.kick(reason=" "+reason)

@client.command()
async def clear(ctx,amount=10):
  await ctx.channel.purge(limit = amount)
#-------------------- RANDOM COMMANDS --------------------------------------
@client.command()
async def ping(ctx):
  newembed = discord.Embed(title = f'Your ping is `{round(client.latency*1000)}` ms')
  await ctx.send(embed = newembed)


@client.command(aliases=['userinfo', 'info', 'user', 'tma'])
async def whois(ctx, member: discord.Member):
    embed = discord.Embed(
        title=member.name, description=member.mention)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)


client.run("NAH, TOKEN")
