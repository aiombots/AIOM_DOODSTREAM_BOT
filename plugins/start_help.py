#!/usr/bin/env python3


### Importing
from pyrogram import Client, filters
from pyrogram.types import Message
from main import Main


@app.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text("")

@app.on_message(filters.command("help"))
async def help_message(bot, message):
    await message.reply_text("")

