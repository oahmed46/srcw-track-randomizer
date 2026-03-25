# CrossBot
- Discord Bot using discord.py (REST API) for custom functionality to support the [Sonic Racing: Crossworlds Discord Server](https://discord.gg/sonicracingcrossworlds)
- Python based script for randomizing csv inputs (columns only)
- Test Data included - Main Courses and CrossWorlds csv files from Sonic Racing: CrossWorlds

# Setup

1. Install necessary python modules
```
pip install -r requirements.txt
```
2. Create a `.env` file in the project root.
3. Copy the content of `.env.example` to `.env`.
4. Fill in your actual tokens.

.env.example:
```
DISCORD_BOT_TOKEN=your_token_here
TEST_GUILD_ID=your_guild_id_here
STAGE_RING_RANDOM = your_path_to_image.png
```
