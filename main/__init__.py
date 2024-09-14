from pyrogram import Client as PyrogramClient
from telethon import TelegramClient
from telethon.sessions import StringSession
import sys
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# variables
API_ID = 21334875
API_HASH = "9cfc4c8a72b8a7edbcf4d5e235f729c6"
BOT_TOKEN = "7485655503:AAGWfiYHnfyziPyVsifUv_bnOgMIXIHPep4"
SESSION = "1AZWarzoBuw72SFz3fhQlwp9h5v_aC5FKfSt8ZM0F3A40WieGK9ficKZXKFBYM62T7hVGt0Ant6ZU0xW1v2YfsEuKyVYkoSQHxjPLcD2CoLbgxsg2I165kHiglFybzIK5kFz_ZY2VS5kA0T4-QpkppwHxy-PtAZtRBRd_JNvBRdmcDImAr0oCzjaw3GxdlT2VD0XJkmOKPIdL07nXo4LSB-QmDtsOOfKD4__d89Z1g1X1hnNTRmUCHx6P4jfuMW6jeB99Z_xQ2-h1a9PE19E1cUTVxwY_jJ_Cmg1LtkCvr8dQAfWr6wMxQR1wf5nDJHw1sOFNpAB3LRmyifiY4NsZy6LsHo4HfYs="
FORCESUB = "NDA_Shaurya2025"
AUTH = "6902509496"

# Initialize and start the Telethon userbot
try:
    userbot = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
    userbot.start()
    print("Telethon userbot started successfully!")
except Exception as e:
    print(f"Userbot Error! {str(e)} Have you added SESSION while deploying??")
    sys.exit(1)

# Initialize and start the Pyrogram bot
try:
    bot = PyrogramClient("SaveRestricted", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)
    bot.start()
    print("Pyrogram bot started successfully!")
except Exception as e:
    print(f"Bot Error! {str(e)}")
    sys.exit(1)
  
