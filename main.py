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

@bot.tree.command(
    name = "menu",
    description="View da menu and prace ya order",
)
async def menu(interaction: discord.Interaction):
    embed = discord.Embed(
        title="City Wok",
        description="Herro, Wercome to City Wok, Take ur order pree?",
        color=discord.Color.orange()
    )

    embed.add_field(
        name="City Mains",
        value="**City Chicken** - 12 Dorrar\n**City Beef** - 15 Dorrar\n**City Shrimp** - 11 Dorrar\n**Super Spicy City Shrimp** - 26 Dorrar\n**City Teriyaki Chicken** - 24 Dorrar\n**City Sweet and Sour Pork** - 20 Dorrar\n**City Hot and Sour Soup** - 20 Dorrar",
        inline=False,
    )

    embed.add_field(
        name="City Sides",
        value="**City Rice** - 5 Dorrar\nYe dats all we got",
        inline=False,
    )

    embed.add_field(
        name="City Merchandise",
        value="***City Suit*** - 32 Dorrar\n***City Headband*** - 20 Dorrar\n***City Wristband*** - 42 Dorrar",
        inline=False,
    )

    await interaction.response.send_message(embed=embed)


bot.run(TOKEN)