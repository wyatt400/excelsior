import discord
import account_interactions as acc
from keep_alive import keep_alive
from discord.ext import commands
import os

intents = discord.Intents.all()
client = commands.Bot(command_prefix=["ex!", "Ex!"],
                      case_insensitive=True,
                      intents_members=True)
c_name = "Excelsioran Excels"

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('ex!help - Created by the Government of Gapla for the Government of Excelsior'))
    print("Excelsior Bot is ready. \n")


@client.command(help="Checks yours or other people's balances")
async def bal(ctx, user:discord.Member=None):
  if user == None:
    await ctx.send(f"`{str(ctx.author)} has : [{acc.bal(str(ctx.author.id))}] Excelsioran Excels!`")
  else:
    user = str(user.mention)
    a = user.replace("<","")
    a = a.replace(">","")
    a = a.replace("@","")
    a = a.replace("!","")
    user = await client.fetch_user(a)
    await ctx.send(f"`{user} has [{acc.bal(str(user.id))}] Excelsioran Excels!`")

@client.command(help="The command to allow admins to add or subtract money from your balance")
async def add(ctx, amount, user:discord.Member=None):
  if str(ctx.author.id) == "806666676023066678" or str(ctx.author.id) == "838104737642971178":
    user = str(user.mention)
    a = user.replace("<","")
    a = a.replace(">","")
    a = a.replace("@","")
    a = a.replace("!","")
    user = await client.fetch_user(a)
    await ctx.send(f"`{user} now has [{acc.add(str(user.id), amount)}] Excelsioran Excels!`")
  else:
    await ctx.send("`you no admin, so stop try to rob bank`")

@client.command(help="Lets the admins set your bank account balance")
async def set(ctx, amount, user:discord.Member=None):
  if str(ctx.author.id) == "554081235245334534": 
    user = str(user.mention)
    a = user.replace("<","")
    a = a.replace(">","")
    a = a.replace("@","")
    a = a.replace("!","")
    user = await client.fetch_user(a)
    await ctx.send(f"`{user} now has [{acc.set(str(user.id), amount)}] Excelsioran Excels!`")
  else:
    await ctx.send("`you no admin, so stop try to rob bank`")

@client.command(help="Gift other people Excelsioran Excels!")
async def gift(ctx, amount, user:discord.Member=None):
  if user == None:
    await ctx.send("`Please enter a VALID username!`")
  else:
    user = str(user.mention)
    a = user.replace("<","")
    a = a.replace(">","")
    a = a.replace("@","")
    a = a.replace("!","")
    user = await client.fetch_user(a)
    ou = acc.gift(str(ctx.author.id), amount, str(user.id))
    print(ou)
    if ou == "AC":
      await ctx.send(f"`{str(ctx.author)} now has [{acc.bal(str(ctx.author.id))}] Excelsioran Excels and {str(user)} now has [{acc.bal(str(user.id))}] Excelsioran Excels`")
    else:
      await ctx.send("`invalid balance/negative amount`")

@client.command(help="Become a citizen of Excelsior!")
async def citizen(ctx):
	await ctx.send("Link: https://docs.google.com/forms/d/e/1FAIpQLSf8HqfnhMuphnXC60V_G0F8EL0pTUEMxrlks0_N0SBFkcQmDQ/viewform")

@client.command(help="View the latest Excelsioran News from the ENNN!")
async def news(ctx):
	await ctx.send("Link: https://www.excelsiorgov.org/news")

@client.command(help="View Excelsior's website!")
async def website(ctx):
	await ctx.send("Link: https://www.excelsiorgov.org")

@client.command(help="View Excelsior's MicroWiki page!")
async def wiki(ctx):
	await ctx.send("Link: https://micronations.wiki/wiki/Excelsior")

keep_alive()
client.run(os.environ['newkey'])
