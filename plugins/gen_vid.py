from pyrogram import Client, filters
from VideoGen import LLVA

@Client.on_message(filters.command("genvid"))
async def generate_video(client, message):
    if len(message.command) < 2:
        await message.reply("Please provide a prompt for the video.")
        return

    prompt = " ".join(message.command[1:])  
    api_key = "horridapi_OnZUaktXF2FYBAMqEAvoEw_free_key"

    processing_message = await message.reply("Generating video...")

    try:
        k = LLVA(prompt=prompt, api_key=api_key)
        video_path = k.generate_video()
        await message.reply_video(video_path)
        await processing_message.delete()
    except Exception as e:
        await message.reply(f"Error generating video: {e}")