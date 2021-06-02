"""This module contains some functions to use a discord chessbot"""

import chess
import chess.engine
import chess.svg

from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command(name="calculate_fen")
async def calculate_fen(ctx, *fen_notation):
    """This function analyzes a given board given in fen notation and gives the best move"""
    fen_notation = ' '.join(fen_notation)
    engine = chess.engine.SimpleEngine.popen_uci("stockfish")
    board = chess.Board(fen_notation)
    info = engine.analyse(board, chess.engine.Limit(depth=20))
    information = str(info["pv"])
    await ctx.send(information[16:20])
    engine.quit()
    

#@bot.command(name="calculate_pgn")
#async def calculate_pgn(ctx, pgn_notation:str):
#    """This function analyzes a given board given in pgn notation and gives the best move"""
#    await ctx.send(pgn_notation)

with open("CHESSBOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)