#!/usr/bin/env python3


### Importing
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text(
        text="Hᴇʟʟᴏ 👋,\n\nTʜɪs Is A Dᴏᴏᴅ Sᴛʀᴇᴀᴍ Uᴘʟᴏᴀᴅᴇʀ Bᴏᴛ\n\nYᴏᴜ Cᴀɴ Uᴘʟᴏᴀᴅ Vɪᴅᴇᴏ Fʀᴏᴍ Dɪʀᴇᴄᴛ/Rᴀᴡ Uʀʟ Tᴏ Dᴏᴏᴅ Dᴛʀᴇᴀᴍ\n\nCʟɪᴄᴋ Oɴ /help Fᴏʀ Mᴏʀᴇ Dᴇᴛᴀɪʟs\n\nPᴏᴡᴇʀᴅ Bʏ : @AIOM_BOTS",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url="https://t.me/AIOM_BOTS"),
            InlineKeyboardButton("Gʀᴏᴜᴘ", url="https://t.me/AIOM_BOTS_GROUP")
            ],[
            InlineKeyboardButton("Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://github.com/aiombots/AIOM_DOODSTREAM_BOT/edit/master/plugins/start_help.py")
            ]]
            )
       )

@Client.on_message(filters.command("help"))
async def help_message(bot, message):
    await message.reply_text(
        text="Hᴏᴡ Tᴏ Usᴇ Mᴇ?\n\n1. Aᴅᴅ Yᴏᴜʀ Aᴘɪ Kᴇʏ Bʏ Usɪɴɢ /add Aᴘɪᴋᴇʏ\n(<a href='https://doodstream.com/settings'>Gᴇɴᴇʀᴀᴛᴇ Yᴏᴜʀ Aᴘɪ Kᴇʏ Fʀᴏᴍ Hᴇʀᴇ</a>).\n\n2.Nᴏᴡ Sᴇɴᴅ Aɴʏ Dɪʀᴇᴄᴛ Oʀ Rᴀᴡ Uʀʟ Oꜰ Aɴʏ Vɪᴅᴇᴏ\n\n(Iꜰ Yᴏᴜ Wᴀɴᴛ Tᴏ Aᴅᴅ Aɴʏ Cᴜsᴛᴏᴍ Nᴀᴍᴇ Fᴏʀ Vɪᴅᴇᴏ Tʜᴇɴ Sᴇɴᴅ Tʜᴀᴛ Cᴜsᴛᴏᴍ Nᴀᴍᴇ Aʟᴏɴɢ Wɪᴛʜ Uʀʟ Sᴇᴘᴀʀᴀᴛᴇᴅ Bʏ | ᴇ.ɢ., https://example.com/file.mp4 | Cᴜsᴛᴏᴍ Nᴀᴍᴇ)\n\n3.Iꜰ Yᴏᴜ Wᴀɴᴛ Tᴏ Rᴇᴍᴏᴠᴇ Yᴏᴜʀ Aᴘɪ Kᴇʏ Fʀᴏᴍ Bᴏᴛ Tʜᴇɴ Usᴇ /revoke\n\nIꜰ Fᴀᴄɪɴɢ Aɴʏ Pʀᴏʙʟᴇᴍ Tʜᴇɴ Asᴋ Aᴛ : @AIOM_BOTS",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Gᴇɴᴇʀᴀᴛᴇ Yᴏᴜʀ Aᴘɪ Kᴇʏ", url="https://doodstream.com/settings")
            ],[
            InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url="https://t.me/AIOM_BOTS"),
            InlineKeyboardButton("Gʀᴏᴜᴘ", url="https://t.me/AIOM_BOTS_GROUP")
            ]]
            )
       )
