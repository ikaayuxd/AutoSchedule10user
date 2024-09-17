import re
from .. import client, client2
from telethon import TelegramClient, events, functions, types
import asyncio

# Define your channel IDs as a single variable
CHANNEL_IDS = [-1001966404031, -1002495106403] # Replace with your actual channel IDs

@client.on(events.NewMessage)
@client2.on(events.NewMessage)
async def handler(event):
    if event.is_channel: # Check if the message is from a channel
        # Check if the channel ID is in the list
        if event.chat_id in CHANNEL_IDS:
            try:
                await client(functions.messages.SendReactionRequest(
                    peer=event.chat_id,
                    msg_id=event.id,
                    big=True,
                    add_to_recent=True,
                    reaction=[types.ReactionEmoji(emoticon='❤️')]
                ))
                print(f"Reacted to message from {event.chat.title} with ❤️")

                await asyncio.sleep(2) # Flood wait of 2 seconds before the next reaction

            except Exception as e:
                print(f"Error: {e}")
