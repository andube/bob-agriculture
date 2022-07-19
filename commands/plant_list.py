import discord, random, time
from discord.ext import commands
from replit import db
from lists import plants as plants_list
from db_func import plant_crop, handle_timestamp

@commands.command(aliases = ["pl"])
async def plant_list(ctx):
  handle_timestamp(str(ctx.author.id))
  try:
    if int(time.time()) >= int(db[str(ctx.author.id)]['timestamp']) + (48*60*60):
      await ctx.author.send("Your plants have died. You now have no plants")
      db[str(ctx.author.id)]['plant_farm'] = []
      return
  except: 
    await ctx.send('ha plant water go wa\'a ba\'ul')
    
  if db[str(ctx.author.id)]['plant_farm'] == []:
    chosen_crop = random.choice(plants_list) # how did i forget about that
    await ctx.send(f"You didn't have any plants so we're giving you a starter plant\n\nYou got a **{chosen_crop['emoji']}{chosen_crop['name']}**")
    plant_crop(str(ctx.author.id), chosen_crop)
    return
  else:
    plants = ''
    for i, plant in enumerate(db[str(ctx.author.id)]['plant_farm']): # why idk why
      if i % 3 != 0:
        plants += f"  {plant['emoji']} **{plant['name']}**"
      else: 
        plants += f"\n\n{plant['emoji']} **{plant['name']}**"

    await ctx.send(embed = discord.Embed(title = f"{ctx.author.display_name}'s sad plant farm", description = plants, color = discord.Colour.purple()))

def setup(bot):
  bot.add_command(plant_list)