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
    await message.reply_text("Hᴏᴡ Tᴏ Usᴇ Mᴇ?\n\n1. Aᴅᴅ Yᴏᴜʀ Aᴘɪ Kᴇʏ Bʏ Usɪɴɢ /add Aᴘɪᴋᴇʏ\n(Gᴇɴᴇʀᴀᴛᴇ Yᴏᴜʀ Aᴘɪ Kᴇʏ Fʀᴏᴍ Hᴇʀᴇ).\n\n2.Nᴏᴡ Sᴇɴᴅ Aɴʏ Dɪʀᴇᴄᴛ Oʀ Rᴀᴡ Uʀʟ Oꜰ Aɴʏ Vɪᴅᴇᴏ\n\n(Iꜰ Yᴏᴜ Wᴀɴᴛ Tᴏ Aᴅᴅ Aɴʏ Cᴜsᴛᴏᴍ Nᴀᴍᴇ Fᴏʀ Vɪᴅᴇᴏ Tʜᴇɴ Sᴇɴᴅ Tʜᴀᴛ Cᴜsᴛᴏᴍ Nᴀᴍᴇ Aʟᴏɴɢ Wɪᴛʜ Uʀʟ Sᴇᴘᴀʀᴀᴛᴇᴅ Bʏ | ᴇ.ɢ., https://example.com/file.mp4 | Cᴜsᴛᴏᴍ Nᴀᴍᴇ)\n\n3.Iꜰ Yᴏᴜ Wᴀɴᴛ Tᴏ Rᴇᴍᴏᴠᴇ Yᴏᴜʀ Aᴘɪ Kᴇʏ Fʀᴏᴍ Bᴏᴛ Tʜᴇɴ Usᴇ /revoke")

