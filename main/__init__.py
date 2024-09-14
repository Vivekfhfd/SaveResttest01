from pyrogram import Client as PyrogramClient
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from decouple import config
import logging
import sys

# Configure logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# Variables
API_ID = int(config('API_ID', default=21334875))  # Use environment variables or hardcode values
API_HASH = config('API_HASH', default="9cfc4c8a72b8a7edbcf4d5e235f729c6")
BOT_TOKEN = config('BOT_TOKEN', default="7485655503:AAGWfiYHnfyziPyVsifUv_bnOgMIXIHPep4")
SESSION = config('SESSION', default="AQFFi1sAVZmhz3pzJCuVjYo-y43K-MmFmj5mhqN1fnPd6xUOc1RsZNYoM0_Q29GIcrENKSHr7iSw822WQPc8IggM1e173TFeU5GWMa5yGzFHM7_VdN8MbnMmPkfxwuy74f0R1qsYOC9Nt4PfSsptZqbTFCJrFhQ4rW6_QLxkZrE2rUtzaQOOc4Cx1W6HW6JZhxz7dIvF5myWNjw7sZ2Lxqq9R5i3CxuejmlBOrezrqsRqQTY_Mau71RwRdnZQHduHYPIzpnIRQcN_Mu9GpSUAzzFIy1iDCMbJUQowjthMX0b9qHDh5Zf2vlinFULbO45am2fCogXxaHUR8LTHGhVoYRsb0bN7QAAAAGba4AA")
FORCESUB = config('FORCESUB', default="NDA_Shaurya2025")
AUTH = config('AUTH', default="6902509496")

# Initialize the Telethon bot
try:
    bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
    logging.info("Telethon bot started successfully.")
except Exception as e:
    logging.error(f"Failed to start Telethon bot: {e}")
    sys.exit(1)

# Initialize the Pyrogram userbot
try:
    userbot = PyrogramClient("saverestricted", session_string=SESSION, api_id=API_ID, api_hash=API_HASH)
    userbot.start()
    logging.info("Pyrogram userbot started successfully.")
except Exception as e:
    logging.error(f"Failed to start Pyrogram userbot: {e}")
    sys.exit(1)

# Optional: Initialize another Pyrogram client (if needed)
try:
    Bot = PyrogramClient("SaveRestricted", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)
    Bot.start()
    logging.info("Pyrogram bot started successfully.")
except Exception as e:
    logging.error(f"Failed to start Pyrogram bot: {e}")
    sys.exit(1)
    
