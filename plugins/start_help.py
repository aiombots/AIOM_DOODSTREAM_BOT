#!/usr/bin/env python3


### Importing
from pyrogram import Client, filters
from pyrogram.types import Message
from main import Main


@app.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text("Hᴇʟʟᴏ 👋,\n\nTʜɪs Is A Dᴏᴏᴅ Sᴛʀᴇᴀᴍ Uᴘʟᴏᴀᴅᴇʀ Bᴏᴛ\n\nYᴏᴜ Cᴀɴ Uᴘʟᴏᴀᴅ Vɪᴅᴇᴏ Fʀᴏᴍ Dɪʀᴇᴄᴛ/Rᴀᴡ Uʀʟ Tᴏ Dᴏᴏᴅ Dᴛʀᴇᴀᴍ\n\nCʟɪᴄᴋ Oɴ /help Fᴏʀ Mᴏʀᴇ Dᴇᴛᴀɪʟs\n\nPᴏᴡᴇʀᴅ Bʏ : @AIOM_BOTS")

@app.on_message(filters.command("help"))
async def help_message(bot, message):
    await message.reply_text("")

