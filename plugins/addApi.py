#!/usr/bin/env python3


### Importing
from botModule.importCommon import *


### Start & Help Handler
@Client.on_message(filters.private & filters.command("add"))
async def addApiHandler(bot:Update, msg:Message):
    if await search_user_in_community(bot, msg):
        splitMessage = msg.text.split(' ')
        if len(splitMessage) == 2:
            userid = msg.chat.id
            if not apiExist(userid):
                apiKey = splitMessage[1]
                if await isApiValid(apiKey, bot, msg):
                    addApiKey(apiKey, userid)
                    await msg.reply_text(
                        "<b>Yᴏᴜʀ Aᴘɪ Kᴇʏ Hᴀs Bᴇᴇɴ Aᴅᴅᴇᴅ Sᴜᴄᴄᴇssꜰᴜʟʟʏ</b>",
                        parse_mode = "html"
                    )
            else:
                await msg.reply_text(
                    "<b>Yᴏᴜʀ Aᴘɪ Kᴇʏ Is Aʟʀᴇᴀᴅʏ Aᴅᴅᴇᴅ</b>",
                    parse_mode = "html"
                )
        else:
            await msg.reply_text(
                "<b>Iɴᴠᴀʟɪᴅ Cᴏᴍᴍᴀɴᴅ\nSᴇɴᴅ Aᴘɪ Kᴇʏ Lɪᴋᴇ Tʜɪs <code>/add APIKEY</code>\n\nFᴏʀ Sᴜᴘᴘᴏʀᴛ Asᴋ Aᴛ : @AIOM_BOTS_GROUP</b>",
                parse_mode = "html"
            )
    return

