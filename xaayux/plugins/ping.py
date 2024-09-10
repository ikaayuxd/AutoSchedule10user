import re
from .. import client
import asyncio
from telethon import TelegramClient, events, types 
from telethon.tl.functions.messages import SendReactionRequest 

@client.on(events.NewMessage) 
async def reaction_handler(event):
    chat = await event.get_chat()
    message_id = event.id

    try:
        await client(SendReactionRequest(
            peer=chat,
            msg_id=message_id,
            reaction='❤' # Pass the emoji directly as a string 
        ))
    except Exception as e:
        print(f"Error sending reaction: {e}") 
