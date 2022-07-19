import discord, asyncio
import main
from discord.ext import commands
from replit import db
from db_func import check_valid

@commands.command(aliases = ["al"])
async def animal_list(ctx, bot = main.bot):
  if str(ctx.author.id) in db.keys():
    check_valid(str(ctx.author.id))
    
    pages = ['']
    page, animals = 0, 0
    for i, animal in enumerate(db[str(ctx.author.id)]['animals']):

      animals += animal["amount"]
      
      pages[page] += f'{animal["emoji"]} **{animal["name"]}** `x{animal["amount"]}`\n'
      
      if (i + 1) % 10 == 0 and i != len(db[str(ctx.author.id)]['animals']) - 1: 
        page += 1
        pages.append('')
    
    page = 0
    
    msg = await ctx.send(embed = discord.Embed(title=f"{ctx.author.display_name}'s Yucky Farm. Amount: {str(animals)}", description=pages[0], color = discord.Colour.green()).set_footer(text=f'Page 1 of {len(pages)}'))
    
    await msg.add_reaction('◀️')
    await msg.add_reaction('▶️')
    def lecheck(reaction, user):
      return user.id == ctx.author.id and str(reaction.emoji) in ['◀️','▶️']
    
    while True:
      try:
        react, u = await bot.wait_for('reaction_add', timeout=40, check=lecheck)
  
        await msg.remove_reaction(react, u)
        
        if str(react.emoji) == '▶️' and page != len(pages) - 1:
          page += 1
          await msg.edit(embed=discord.Embed(title=f"{ctx.author.display_name}'s Yucky Farm. Amount: {str(animals)}", description=pages[page], color=discord.Colour.green()).set_footer(text=f'Page {page + 1} of {len(pages)}'))

        elif str(react.emoji) == '◀️' and page != 0:
          page -= 1
          await msg.edit(embed=discord.Embed(title=f"{ctx.author.display_name}'s Yucky Farm. Amount: {str(animals)}", description=pages[page], color=discord.Colour.green()).set_footer(text=f'Page {page + 1} of {len(pages)}'))

      except asyncio.TimeoutError:

        await msg.remove_reaction("▶️", bot.user)
        await msg.remove_reaction("◀️", bot.user)
  else:
    await ctx.send('Start a farm with `bob!catch` if you wanna view a list of animals.')

def setup(bot):
  bot.add_command(animal_list)