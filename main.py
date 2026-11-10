import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="/",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

    await bot.tree.sync()

bot.run(TOKEN)