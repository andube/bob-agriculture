import discord
from discord.ext import commands
from replit import db

@commands.command()
async def circles(ctx):
  if db[str(ctx.author.id)]["circles"] == []:
    await ctx.send("Circleless bozo lmao")
    return
  circle_desc = ''
  for i, circle in enumerate(db[str(ctx.author.id)]["circles"]):
    if i % 3 != 0:
      circle_desc += f"{circle}  "
    else:
      circle_desc += f"\n\n{circle}"

  await ctx.send(embed = discord.Embed(title = f"{ctx.author.display_name}'s Beautiful Circle Collection", description = circle_desc, color = discord.Colour.yellow()))

def setup(bot):
  bot.add_command(circles)