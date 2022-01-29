#!/usr/bin/env python3


### Importing
from botModule.importCommon import *


### Start & Help Handler
@Client.on_message(filters.private & filters.regex(r'^http(.*)'))
async def urlUploaderHandler(bot:Update, msg:Message):
    if await search_user_in_community(bot, msg):
        userid = msg.chat.id
        result = apiExist(userid)
        if result:
            apiKey = result['apiKey']
            apiUrl = f"https://doodapi.com/api/upload/url?key={apiKey}"
            message = msg.text
            if '|' in message:
                url, filename = message.split("|")
                filename = filename.strip()
                if " " in filename:
                    filename = '_'.join(filename.split(' '))
                apiUrl += f"&new_title={filename}"
            else:
                url = msg.text
                if " " in url:
                    return await msg.reply_text(
                        "<b>Gɪᴠᴇɴ Uʀʟ Is Iɴᴠᴀʟɪᴅ.</b>",
                        parse_mode = "html"
                    )
            url = url.strip()
            apiUrl += f"&url={url}"
            fileID = uploadRequest(apiUrl)
            if fileID:
                fileurl = f'https://dood.la/d/{fileID}'
                await msg.reply_text(
                    f"<b>Yᴏᴜʀ Fɪʟᴇ Wɪʟʟ Bᴇ Uᴘʟᴏᴀᴅᴇᴅ Sᴏᴏɴ Oɴ Tʜɪs Uʀʟ :\n<code>{fileurl}</code></b>",
                    parse_mode = "html"
                )
            else:
                await msg.reply_text(
                    "<b>Uɴᴀʙʟᴇ Tᴏ Uᴘʟᴏᴀᴅ Yᴏᴜʀ Fɪʟᴇ. Sᴏᴍᴇᴛʜɪɴɢ Wᴇɴᴛ Wʀᴏɴɢ.</b>",
                    parse_mode = "html"
                )
        else:
            await msg.reply_text(
                "<b>Yᴏᴜʀ Aᴘɪ Kᴇʏ Is Nᴏᴛ Aᴅᴅᴇᴅ\nAᴅᴅ Yᴏᴜʀ Aᴘɪ Kᴇʏ Bʏ Usɪɴɢ <code>/add APIKEY</code>.</b>",
                parse_mode = "html"
            ) 
    return

