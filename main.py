import discord, os, keep_alive
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "bob!", case_insensitive = True, intents = intents)


@bot.event
async def on_ready():
  print("\033c")
  print(f"{bot.user} is here!")



bot.load_extension("commands.animal_list")
bot.load_extension("commands.animal")
bot.load_extension("commands.plant_list")
bot.load_extension("commands.plant")
bot.load_extension("commands.circles") # john cena below?
print("bro the commands are loaded tbh") # ITS JOHN CENA

keep_alive.keep_alive()


bot.run(os.getenv('TOKEN'))
