import re
from .. import client, client2 # Import both clients
from telethon import TelegramClient, events, functions, types
import asyncio

# Define your channel IDs as a single variable
CHANNEL_IDS = [-1001966404031, -1002495106403] # Replace with your actual channel IDs

@client.on(events.NewMessage(chats=CHANNEL_IDS))
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
            print(f"Client 1 reacted to message from {event.chat.title} with ❤️")
            await asyncio.sleep(2)
        except Exception as e:
            print(f"Client 1 Error: {e}")

@client2.on(events.NewMessage(chats=CHANNEL_IDS))
async def handler_client2(event):
    if event.is_channel:
        try:
            await event.client(functions.messages.SendReactionRequest(
                peer=event.chat_id,
                msg_id=event.id,
                big=True,
                add_to_recent=True,
                reaction=[types.ReactionEmoji(emoticon='🥰')]
            ))
            print(f"Client 2 reacted to message from {event.chat.title} with 🥰")
            await asyncio.sleep(2)
        except Exception as e:
            print(f"Client 2 Error: {e}")


with client:
    client.run_until_disconnected()

with client2:
    client2.run_until_disconnected()
