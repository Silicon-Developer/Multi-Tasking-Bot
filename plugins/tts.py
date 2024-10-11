import os, requests
from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup , ForceReply


def detect_language(text):
    try:
        data = {"text": text} 
        response = requests.post("https://bisal-ai-api.vercel.app/lang", data=data)
        return response.text
    except Exception as e:
        return "hi"

@Client.on_message(filters.command("tts") & filters.private)
async def tts(client, message):
    try:
        msg = await client.ask(message.chat.id, "<b>sᴇɴᴅ ᴍᴇ ᴀ ᴛᴇxᴛ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ɪɴᴛᴏ ᴀᴜᴅɪᴏ ғɪʟᴇ.</b>" , reply_to_message_id = message.id, filters = filters.text ,
                               reply_markup =ForceReply(True))
        if not msg.text:
            return await message.reply("sᴇɴᴅ ᴍᴇ ᴀ ᴛᴇxᴛ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ɪɴᴛᴏ ᴀᴜᴅɪᴏ ғɪʟᴇ ᴀғᴛᴇʀ ɢɪᴠɪɴɢ /tts ᴄᴏᴍᴍᴀɴᴅ")
        m = await message.reply("<b>Cᴏɴᴠᴇʀᴛɪɴɢ...</b>")
        toConvert = msg.text.replace("\n", " ").replace("`", "")
        lang = detect_language(toConvert)
        if lang == 'en' or lang == 'hi':
            voice = "en-US-JennyNeural" if lang == 'en' else "hi-IN-SwaraNeural"
            command = f'edge-tts --voice \"{voice}\" --text \"{toConvert}\" --write-media \"tts.mp3\"'
            os.system(command)
        else:
            voice = "hi-IN-SwaraNeural"
            command = f'edge-tts --voice \"{voice}\" --text \"{toConvert}\" --write-media \"tts.mp3\"'
            os.system(command)
        await m.delete()
        await message.reply_voice("tts.mp3")
        os.remove("tts.mp3")
    except Exception as e:
        await m.edit('<b>sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ ! ᴘʟᴇᴀsᴇ ᴜsᴇ ᴅɪғғᴇʀᴇɴᴛ ᴛᴇxᴛs\nᴏʀ ʀᴇᴘᴏʀᴛ ɪɴ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ: @Brutal_Support</b>')
        print('err in tts',e)
        try:
            os.remove("tts.mp3")
        except:pass