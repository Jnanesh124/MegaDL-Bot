import os
from pyrogram import Client, filters
from config import Config

@Client.on_message(filters.reply & filters.text & filters.private)
async def newcap(bot, message):
    nc = message.reply_to_message
    # Check if the replied message contains media and is not a video note or sticker
    if nc.media and not (nc.video_note or nc.sticker):
        await nc.copy(message.chat.id, caption=message.text)
