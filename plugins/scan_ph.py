import requests 
from Mangandi import ImageUploader
from pyrogram import Client, filters

api = "https://horridapi.onrender.com/search"

@Client.on_message(filters.command("scan_ph"))
async def scan_ph(client, message):
    reply = message.reply_to_message    
    if not reply:
        return await message.reply_text("**Reply to a photo to use this command!**")
    elif not reply.photo:
        return await message.reply_text("**Reply to a photo to use this command!**")
    elif reply.video:
        return await message.reply_text("**Reply to a photo to use this command!**")   
    query = message.text.split(" ", 1)[1] if len(message.text.split(" ")) > 1 else ""    
    if not query:
        await message.reply("**Provide query! like `/scan_ph tell me about of this image`**")
        return
    k = await message.reply_text(f"**Hey {message.from_user.mention}, Wait Iam Checking **")
    media = await reply.download()
    m = await k.edit("**Successfully Checked Your query**")
    mag = ImageUploader(media)
    img_url = mag.upload()                   
    response = requests.get(f"{api}?img={img_url}&query={query}")   
    result = response.json()
    await m.edit(f"**Hey {message.from_user.mention},\n\n{result['response']}**")