from stockfish import Stockfish
from discord.ext import commands


stockfish = Stockfish("/Users/aadarshkrishnan/discord-chatbox/stockfish/stockfish-9-64")

bot = commands.Bot(command_prefix='!')

@bot.command(name = "calculate", help = "set up position to calculate using FEN notation")
async def calculate(ctx, notation: str):
    stockfish.set_fen_position(notation)
    await ctx.send(stockfish.get_best_move)

with open ("CHESSBOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read
    print("Token file read")
    bot.run(TOKEN)
