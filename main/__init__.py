from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Variables
API_ID = 21334875
API_HASH = "9cfc4c8a72b8a7edbcf4d5e235f729c6"
BOT_TOKEN = "7485655503:AAGWfiYHnfyziPyVsifUv_bnOgMIXIHPep4"
SESSION = "1AZWarzoBuw72SFz3fhQlwp9h5v_aC5FKfSt8ZM0F3A40WieGK9ficKZXKFBYM62T7hVGt0Ant6ZU0xW1v2YfsEuKyVYkoSQHxjPLcD2CoLbgxsg2I165kHiglFybzIK5kFz_ZY2VS5kA0T4-QpkppwHxy-PtAZtRBRd_JNvBRdmcDImAr0oCzjaw3GxdlT2VD0XJkmOKPIdL07nXo4LSB-QmDtsOOfKD4__d89Z1g1X1hnNTRmUCHx6P4jfuMW6jeB99Z_xQ2-h1a9PE19E1cUTVxwY_jJ_Cmg1LtkCvr8dQAfWr6wMxQR1wf5nDJHw1sOFNpAB3LRmyifiY4NsZy6LsHo4HfYs="
FORCESUB = "NDA_Shaurya2025"
AUTH = "6902509496"

# Start the Telethon bot
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Start the Pyrogram userbot with session string
try:
    print("Starting Pyrogram userbot...")
    userbot = Client("saverestricted", session_string=SESSION, api_id=API_ID, api_hash=API_HASH)
    userbot.start()
    print("Userbot started successfully!")
except BaseException as e:
    print(f"Userbot Error! Have you added SESSION while deploying?? Error: {e}")
    sys.exit(1)

# Start the Pyrogram bot
try:
    print("Starting Pyrogram bot...")
    Bot = Client(
        "SaveRestricted",
        bot_token=BOT_TOKEN,
        api_id=int(API_ID),
        api_hash=API_HASH
    )    
    Bot.start()
    print("Bot started successfully!")
except Exception as e:
    print(f"Bot Error: {e}")
    sys.exit(1)
  
