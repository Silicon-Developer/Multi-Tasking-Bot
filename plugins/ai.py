from pyrogram import Client, filters
import requests
import urllib.parse

def ask_query(query, model=None):
    # Default system prompt if using the default model
    default_model = 'claude-sonnet-3.5'
    system_prompt = "You are a helpful assistant. Your name is Asuraa, and your owner's name is Captain, known as @itzAsuraa."

    # Use the provided model or default to 'claude-sonnet-3.5'
    model = model or default_model

    # Manually prepend the system prompt to the user's query
    if model == default_model:
        query = f"{system_prompt}\n\nUser: {query}"

    # URL encode the query
    encoded_query = urllib.parse.quote(query)

    # Construct the full URL
    url = f"https://chatwithai.codesearch.workers.dev/?chat={encoded_query}&model={model}"

    # Make the GET request to the API
    response = requests.get(url)
    
    # Check for successful response
    if response.status_code == 200:
        return response.json().get("result", "No response found.")
    else:
        return f"Error fetching response from API. Status code: {response.status_code}"

# Handler for the "/ai" command
@Client.on_message(filters.command("ai"))
async def handle_query(client, message):
    user_query = message.text.split(maxsplit=1)[1] if len(message.command) > 1 else None

    if not user_query:
        await message.reply_text("<b>Please provide a query to ask.</b>")
        return

    # Fetch the response from the AI API
    response = ask_query(user_query)

    # Send the response back to the user
    await message.reply_text(f"<b>{response}</b>")
