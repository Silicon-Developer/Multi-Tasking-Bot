from requests import get 
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto

@Client.on_message(filters.command(['wall', 'wallpaper', 'wallpapers']))
async def WallpapersCom(client, message):
    chat_id = message.chat.id
    try:
        query = message.text.split(None, 1)[1]
    except IndexError:
        return await message.reply("Input image name for search 🔍")

    msg = await message.reply("🔍")
    
    images = get(f"https://hoshi-api-f62i.onrender.com/api/wallpaper?query={query}").json()
    media_group = []
    count = 0

    if not images:
       return await message.reply_text(
         text=f"**✨ No wallpapers found for query: `{message.text.split(None, 1)[1]}`, Ask other I wish to send you ❤️**"
       )
      
    for url in images["images"][:8]:
        media_group.append(InputMediaPhoto(media=url))
        count += 1
    
    await msg.edit(f"⚡ Fetched {count} wallpapers...")
    
    try:
        await client.send_media_group(
            chat_id=chat_id, 
            media=media_group,
            reply_to_message_id=message.id
        )
        return await msg.delete()
    except Exception as e:
        await msg.delete()
        return await message.reply(f"Error\n{e}")

__mod_name__ = "Wall"

__help__ = f"""
⚡ **Wallpapers**:

Command: /wall, /wallpaper
with Query. will send you maximum 8 images as media group.

by @Silicon_Bot_Update 
"""
