from pyrogram import Client, filters
import requests
import urllib.parse

def ask_query(query, model=None):
    default_model = 'claude-sonnet-3.5'
    system_prompt = "You are a helpful assistant. Your name is Asuraa, and your owner's name is Silicon, known as @Silicon_Botz."

    model = model or default_model

    if model == default_model:
        query = f"{system_prompt}\n\nUser: {query}"

    encoded_query = urllib.parse.quote(query)
    url = f"https://chatwithai.codesearch.workers.dev/?chat={encoded_query}&model={model}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("result", "No response found.")
    else:
        return f"Error fetching response from API. Status code: {response.status_code}"

# Handler for the "/ai" command
@Client.on_message(filters.command("ai"))
def handle_query(client, message):
    user_query = message.text.split(maxsplit=1)[1] if len(message.command) > 1 else None

    if not user_query:
        message.reply_text("<b>Please provide a query to ask.</b>")
        return

    # Fetch the response from the AI API
    response = ask_query(user_query)

    # Send the response back to the user
    message.reply_text(f"<b>{response}</b>")
