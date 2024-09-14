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
SESSION = config('SESSION', default="1AZWarzoBuw72SFz3fhQlwp9h5v_aC5FKfSt8ZM0F3A40WieGK9ficKZXKFBYM62T7hVGt0Ant6ZU0xW1v2YfsEuKyVYkoSQHxjPLcD2CoLbgxsg2I165kHiglFybzIK5kFz_ZY2VS5kA0T4-QpkppwHxy-PtAZtRBRd_JNvBRdmcDImAr0oCzjaw3GxdlT2VD0XJkmOKPIdL07nXo4LSB-QmDtsOOfKD4__d89Z1g1X1hnNTRmUCHx6P4jfuMW6jeB99Z_xQ2-h1a9PE19E1cUTVxwY_jJ_Cmg1LtkCvr8dQAfWr6wMxQR1wf5nDJHw1sOFNpAB3LRmyifiY4NsZy6LsHo4HfYs=")
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
    
