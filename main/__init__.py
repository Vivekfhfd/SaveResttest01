#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 21334875
API_HASH = "9cfc4c8a72b8a7edbcf4d5e235f729c6"
BOT_TOKEN = "7485655503:AAGWfiYHnfyziPyVsifUv_bnOgMIXIHPep4"
SESSION = "AQFFi1sAVZmhz3pzJCuVjYo-y43K-MmFmj5mhqN1fnPd6xUOc1RsZNYoM0_Q29GIcrENKSHr7iSw822WQPc8IggM1e173TFeU5GWMa5yGzFHM7_VdN8MbnMmPkfxwuy74f0R1qsYOC9Nt4PfSsptZqbTFCJrFhQ4rW6_QLxkZrE2rUtzaQOOc4Cx1W6HW6JZhxz7dIvF5myWNjw7sZ2Lxqq9R5i3CxuejmlBOrezrqsRqQTY_Mau71RwRdnZQHduHYPIzpnIRQcN_Mu9GpSUAzzFIy1iDCMbJUQowjthMX0b9qHDh5Zf2vlinFULbO45am2fCogXxaHUR8LTHGhVoYRsb0bN7QAAAAGba4AA"
FORCESUB = "NDA_Shaurya2025"
AUTH = "6902509496"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
