from pyrogram import Client, idle
from dotenv import load_dotenv
import os
load_dotenv("config.env")

plugins = dict(
    root="plugins",
    include=['echo']
)

bot = Client("TestBot",
    api_id=int(os.environ.get('API_ID')),
    api_hash=os.environ.get('API_HASH'),
    bot_token=os.environ.get('BOT_TOKEN'),
    plugins=plugins
)

if __name__ == '__main__':
    bot.start()
    idle()
    bot.stop()