from discord.ext import commands 

import random

bot = commands.Bot(command_prefix= '!')

@bot.command(name = "idea")
async def idea(ctx):
    await ctx.send("Ideas are hard")
    
    topics = ['chat bot', 'cli', 'game', 'web bot', 'brower extension', 'api', 'website']
    areas = ['pet care', 'doing homework', 'fitness']
    idea = f'Create an new {random.choice(topics)} that helps with {random.choice(areas)} :slight_smile:'
    await ctx.send(idea)


with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)