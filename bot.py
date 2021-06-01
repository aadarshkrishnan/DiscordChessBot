from discord.ext import commands 

import random

bot = commands.Bot(command_prefix= '!')

@bot.command(name = "idea", help = "Get a random side project idea")
async def idea(ctx):
    await ctx.send("Ideas are hard")
    
    topics = ['chat bot', 'cli', 'game', 'web bot', 'brower extension', 'api', 'website']
    areas = ['pet care', 'doing homework', 'fitness']
    idea = f'Create an new {random.choice(topics)} that helps with {random.choice(areas)} :slight_smile:'
    await ctx.send(idea)

@bot.command(name = "calc", help = "Do a two number calculation where fn is +, -, /, *, **")
async def calc(ctx, x: float, fn: str, y: float):
    if fn == '+':
        await ctx.send(x + y)
    elif fn == '-':
        await ctx.send(x - y)
    elif fn == '/':
        await ctx.send(x / y)
    elif fn == '*':
        await ctx.send(x * y)
    elif fn == '**':
        await ctx.send(x ** y)

with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)