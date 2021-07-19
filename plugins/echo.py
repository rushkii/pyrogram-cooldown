from pyrogram import Client, filters
from .utils import cooldown

bot = Client

@bot.on_message(filters.command(['test']))
@cooldown.wait(5)
async def echo_text(_,msg):
    await msg.reply(msg.text)
