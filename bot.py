import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

from commands import csv_column_randomizer

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
TEST_GUILD_ID = os.getenv("TEST_GUILD_ID")
STAGE_RING_RANDOM = os.getenv("STAGE_RING_RANDOM")

# Set up Discord bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!',
                   description="Sonic Racing: CrossWorlds Utility Bot",
                   intents=intents)

GUILD_ID_OBJECT = discord.Object(id=TEST_GUILD_ID)


@bot.event
async def on_ready():
    """Event handler for when the bot is ready"""
    # Tell the type checker that User is filled up at this point
    assert bot.user is not None

    # Sync the application commands to the specified guild
    # Allows for faster command registration during development and testing
    try:
        guild = discord.Object(id=TEST_GUILD_ID)
        synced = await bot.tree.sync(guild=guild)
        print(f"Synced {len(synced)} command(s) to the guild '{TEST_GUILD_ID}'")
    except Exception as e:
        print(f"Error syncing commands: {str(e)}")

    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.tree.command(name="courses",
                  description="Generate a random number of Courses",
                  guild=GUILD_ID_OBJECT
                  )
async def random_courses(interaction: discord.Interaction,
                         count: int = 12):
    courses = csv_column_randomizer(number_of_items=count)
    embed = discord.Embed(title=" Random Course Selection",
                          color=discord.Color.from_rgb(0, 60, 180),
                          description=courses)
    file = discord.File(STAGE_RING_RANDOM, filename="image.png")
    embed.set_thumbnail(url="attachment://image.png")
    await interaction.response.send_message(embed=embed, file=file)


bot.run(DISCORD_BOT_TOKEN)
