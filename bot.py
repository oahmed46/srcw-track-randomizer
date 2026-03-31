import os  # default module
import discord

from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

from commands import csv_column_randomizer, csv_column_length

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
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s) synced globally")

        # Sync the application commands to the specified guild
        # Allows for faster command registration during development and testing

        guild = discord.Object(id=TEST_GUILD_ID)
        synced = await bot.tree.sync(guild=guild)
        print(f"Synced {len(synced)} command(s) to the guild '{TEST_GUILD_ID}'")
    except Exception as e:
        print(f"Error syncing commands: {str(e)}")

    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.tree.command(name="courses",
                  description="Generate a random number of Courses"
                  # ,guild=GUILD_ID_OBJECT  # Uncomment this line to register the command to a specific guild for faster updates during development
                  )
@app_commands.describe(count="The number of courses to generate. default = 12")
@app_commands.describe(prevent_duplicates="Whether to prevent duplicate course selection. default = True")
async def random_courses(interaction: discord.Interaction,
                         count: app_commands.Range[int, 1, csv_column_length()] = 12,
                         prevent_duplicates: bool = True):
    courses = csv_column_randomizer(number_of_items=count,
                                    prevent_duplicates=prevent_duplicates)
    embed = discord.Embed(title=" Random Course Selection",
                          color=discord.Color.from_rgb(0, 60, 180),
                          description=courses)
    file = discord.File(STAGE_RING_RANDOM, filename="image.png")
    embed.set_thumbnail(url="attachment://image.png")
    await interaction.response.send_message(embed=embed,
                                            file=file,
                                            delete_after=7200)  # Delete the message after 2 hours (7200 seconds)
    message = await interaction.original_response()
    await message.pin(reason="Pinned by bot: Random Course Selection")


@bot.tree.command(name="courses_thread",
                  description="Generate a random number of Courses"
                  ,guild=GUILD_ID_OBJECT  # Uncomment this line to register the command to a specific guild for faster updates during development
                  )
@app_commands.describe(count="The number of courses to generate. default = 12")
@app_commands.describe(prevent_duplicates="Whether to prevent duplicate course selection. default = True")
async def random_courses_thread(interaction: discord.Interaction,
                         count: app_commands.Range[int, 1, csv_column_length()] = 12,
                         prevent_duplicates: bool = True):
    courses = csv_column_randomizer(number_of_items=count,
                                    prevent_duplicates=prevent_duplicates)
    embed = discord.Embed(title=" Random Course Selection",
                          color=discord.Color.from_rgb(0, 60, 180),
                          description=courses)
    file = discord.File(STAGE_RING_RANDOM, filename="image.png")
    embed.set_thumbnail(url="attachment://image.png")
    channel = bot.get_channel(interaction.channel_id)
    thread = await channel.create_thread(name=f"{discord.utils.utcnow().strftime('%Y-%m-%d %H:%M:%S')} (UTC) - Random Course Selection",
                                         type=discord.ChannelType.public_thread,
                                         reason="Thread for Random Course Selection")
    message = await thread.send(embed=embed, file=file)
    await message.pin(reason="Pinned by bot: Random Course Selection")
    await interaction.response.send_message(f"Random course selection has been posted in {thread.mention} and pinned for easy access.", 
                                            ephemeral=True,
                                            delete_after=7200)  # Delete the message after 2 hours (7200 seconds)
    

bot.run(DISCORD_BOT_TOKEN)
