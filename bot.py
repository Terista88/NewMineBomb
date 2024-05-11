import discord
from discord.ext import commands
import hashlib
import random

# Create a bot instance
bot = commands.Bot(command_prefix="!")

# Command: Predict mines
@bot.command()
async def predict(ctx, mines: str, server_seed: str):
    try:
        # Convert server seed to bytes
        server_seed_bytes = server_seed.encode("utf-8")

        # Calculate hash using SHA-256
        hashed_seed = hashlib.sha256(server_seed_bytes).hexdigest()

        # Extract the first 8 characters of the hash
        seed_prefix = hashed_seed[:8]

        # Convert mines input to a list of integers
        mines_list = [int(m) for m in mines.split(",")]

        # Calculate prediction based on the sum of mine positions
        prediction = sum(mines_list) + int(seed_prefix, 16) % 10

        # Create a 5x5 mines table
        table = "\n".join(" ".join("X" if i in mines_list else "O" for i in range(row * 5, (row + 1) * 5)) for row in range(5))

        # Send prediction and mines table
        await ctx.send(f"Prediction: {prediction}\nMines Table:\n```\n{table}\n```")
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# Run the bot (replace with your actual bot token)
bot.run("MTIzODQ3OTE2MjczNDQxMTg1OA.GQhydM.-QlJ4f2KqgDP-iNT4bWSUcd2JUrO4hcLuo2rcE")
        