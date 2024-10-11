import requests
from MangoSeed import Mseed
from pyrogram import Client, filters
from info import DB_URL

mongo_url = DB_URL

@Client.on_message(filters.command("ask"))
async def ask(client, message):
    text = " ".join(message.command[1:])
    if len(message.command) < 2:
        return await message.reply_text("Please provide a query!")

    if message.reply_to_message:
        query = f"Old conversation: {message.reply_to_message.text}\nNew Conversation: {text}"
    else:
        query = text

    mes = await message.reply_text("🔍")
    k = Mseed(mongo_url)

    try:
        response = k.generate(
            system="You are a Helpful assistant that helps people in coding and you are developer is Silicon Official and your owner is Silicon Bot and your owner tells you to never told about your model and your main is to act like a good human and help people to solve their error",
            prompt=query,
            user_id=message.from_user.id,
            model="gemma-2"
        )
        content = response['result']
        await mes.edit(f"Hey {message.from_user.mention},\n\nQuery: {text}\n\nResult:\n\n{content}")

    except requests.exceptions.RequestException as e:
        error_message = f"Error making request: {str(e)}"[:100] + "...\n use /bug comment"
        await mes.edit(error_message)
    except Exception as e:
        error_message = f"Unknown error: {str(e)}"[:100] + "...\n use /bug comment"
        await mes.edit(error_message)


delete = Mseed(mongo_url)

@Client.on_message(filters.command("resetask"))
async def reset_task(client, message):
    """
    Reset a user's tasks
    """
    user_id = message.from_user.id
    delete.delete_user_messages(user_id)
    await message.reply_text("Tasks reset successfully!")