import discord
from discord.ext import commands
import hashlib

# Create a bot instance
bot = commands.Bot(command_prefix="!")

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")

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

        await ctx.send(f"Prediction: {prediction}")
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# Run the bot
bot.run("MTIzODQ3OTE2MjczNDQxMTg1OA.GQhydM.-QlJ4f2KqgDP-iNT4bWSUcd2JUrO4hcLuo2rcE")
