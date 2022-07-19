import random, time
from discord.ext import commands
from replit import db
from lists import plants, weed
from db_func import check_valid, plant_crop, handle_timestamp

@commands.command(aliases = ["p"])
@commands.cooldown(1, 30, commands.BucketType.user)
async def plant(ctx):
  handle_timestamp(str(ctx.author.id))
    
  if time.time() >= int(db[str(ctx.author.id)]['timestamp']) + (48*60*60):
    await ctx.author.send("Your plants have died. You now have no plants")
    db[str(ctx.author.id)]['plant_farm'] = []
    return

  if db[str(ctx.author.id)]['plant_farm'] == []:
    chosen_crop = random.choice(plants)
    await ctx.send(f"You didn't have any plants so we're giving you a starter plant\n\nYou got a **{chosen_crop['emoji']}{chosen_crop['name']}**")
    db[str(ctx.author.id)]['plant_farm'].append(chosen_crop)
    return
    
  if not random.randint(1, 10) == 7:
    await ctx.send(f"Good job on being a responsible person {ctx.author.display_name}! You have cared for your plants")
  else:
    if random.randint(1, 50) == 40:
      await ctx.send(f"You got {weed['emoji']} **{weed['name']}**. You then got caught by the cops and your entire plant farm was annihalated. L")
      db[str(ctx.author.id)]['plant_farm'] = []
      db[str(ctx.author.id)]['timestamp'] = time.time()
      return
    chosen_crop = random.choice(plants)
    if chosen_crop in db[str(ctx.author.id)]['plant_farm']:
      await ctx.send(f"You WOULD have gotten a {chosen_crop['emoji']} **{chosen_crop['name']}** but when the other {chosen_crop['name']} found out he tried beat him to death.\n\nThe plant narrowly escaped. At least you tended to your existing plants")

    else:
      await ctx.send(f"A {chosen_crop['emoji']} **{chosen_crop['name']}** walked up your farm and shoved itself in the ground.\n\nCheck your farm. Also good job for caring about plants.")
      plant_crop(str(ctx.author.id), chosen_crop)
      
      if db[str(ctx.author.id)]["plant_farm"] == plants:
        add_circle(str(ctx.author.id), "🟢 Green Circle")
        await ctx.send("A 🟢 Green Circle appeared! It's pointless!")
        

@plant.error
async def plant_error(ctx, error):
  await ctx.send(f"Chill. The plants only need so much attention. You can tend to them in {round(error.retry_after)}.")

def setup(bot):
  bot.add_command(plant)