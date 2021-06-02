"""This module contains some functions to use a discord chessbot"""

import chess
import chess.engine

from discord.ext import commands

engine = chess.engine.SimpleEngine.popen_uci("stockfish")

bot = commands.Bot(command_prefix='!')

@bot.command(name="calculate")
async def calculate(ctx, notation: str):
    """This function analyzes a given board and gives the best move"""
    board = chess.Board(notation)
    info = engine.analyse(board, chess.engine.Limit(depth=20))
    information = str(info["pv"])
    await ctx.send(information[16:20])

with open("CHESSBOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)
