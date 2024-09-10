import re
from .. import client
import asyncio
from telethon import TelegramClient, events, types
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import Reaction

@client.on(events.NewMessage)
async def reaction_handler(event):
    chat = await event.get_chat()
    message_id = event.id
    await client(SendReactionRequest(
        peer=chat,
        msg_id=message_id,
        reaction=Reaction(
            emoticon='❤' 
        )
    ))
