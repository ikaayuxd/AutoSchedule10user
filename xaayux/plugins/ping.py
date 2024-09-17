import re
from .. import client, client2# Import both clients
from telethon import TelegramClient, events, functions, types
import asyncio

# Define your channel IDs as a single variable
CHANNEL_IDS = [-1001966404031, -1002495106403] # Replace with your actual channel IDs
@client.on(events.NewMessage(chats=CHANNEL_IDS))
@client2.on(events.NewMessage(chats=CHANNEL_IDS))
async def handler_client1(event):
    if event.is_channel:
        try:
            await event.client(functions.messages.SendReactionRequest(
                peer=event.chat_id,
                msg_id=event.id,
                big=True,
                add_to_recent=True,
                reaction=[types.ReactionEmoji(emoticon='❤️')]
            ))
            await event.client2(functions.messages.SendReactionRequest(
                peer=event.chat_id,
                msg_id=event.id,
                big=True,
                add_to_recent=True,
                reaction=[types.ReactionEmoji(emoticon='❤️')]
            ))
            print(f"Client 1 reacted to message from {event.chat.title} with ❤️")
            await asyncio.sleep(2)
        except Exception as e:
            print(f"Client 1 Error: {e}")
