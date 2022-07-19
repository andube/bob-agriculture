import random
from discord.ext import commands
from replit import db
from lists import plants, animals, catch_quotes
from db_func import plant_crop, add_circle, add_animal


@commands.command(aliases = ["a", "catch"])
@commands.cooldown(1, 60, commands.BucketType.user)
async def animal(ctx):
  
  chosen_animal = random.choice(animals)
  
  if random.randint(1, 30) == 1:
    
    chosen_crop = random.choice(plants)
    
    if chosen_crop not in db[str(ctx.author.id)]['plant_farm']:
      
      await ctx.send(f"You would have gotten a {chosen_animal['emoji']} **{chosen_animal['name']}**!\nBut a {chosen_crop['emoji']} **{chosen_crop['name']}** beat the animal to death.\n\nCheck your farm!")
      
      plant_crop(str(ctx.author.id), chosen_crop)

      if db[str(ctx.author.id)]["plant_farm"] == plants:

        add_circle(str(ctx.author.id), "🟢 Green Circle")
        await ctx.send("A 🟢 Green Circle appeared! It's pointless!")
        
    else:
      await ctx.send(f"You would have gotten a {chosen_animal['emoji']} **{chosen_animal['name']}**!\nBut a {chosen_crop['emoji']} **{chosen_crop['name']}** beat the animal to death.\n\nWhen the other {chosen_crop['name']} found out he beat him to death.")

    return
  
  await ctx.send(f"You got a {chosen_animal['emoji']} **{chosen_animal['name']}**! {random.choice(catch_quotes)}")

  add_animal(str(ctx.author.id), chosen_animal)

  if db[str(ctx.author.id)]["animals"] == animals:

    add_circle(str(ctx.author.id), "🔴 Red Circle")
    await ctx.send("A 🔴 Red Circle appeared! It's the color of animal blood!")



@animal.error
async def animal_error(ctx, error):
  await ctx.send(f'you have to wait {round(error.retry_after)} seconds or ill shit myself')

def setup(bot):
  bot.add_command(animal)
