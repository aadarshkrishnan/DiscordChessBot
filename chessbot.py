import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("stockfish")
board = chess.Board()


board = chess.Board("r1bqkbnr/p1pp1ppp/1pn5/4p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR")
info = engine.analyse(board, chess.engine.Limit(depth=20))
print(info["pv"])

engine.quit()


#from discord.ext import commands

#bot = commands.Bot(command_prefix='!')


#@bot.command(name = "calculate", help = "set up position to calculate using FEN notation")
#async def calculate(ctx, notation: str):
    #print("hi")

#with open ("CHESSBOT_TOKEN.txt", "r") as token_file:
    #TOKEN = token_file.read
    #print("Token file read")
    #bot.run(TOKEN)
