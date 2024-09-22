import re
from .. import client, client2 # Import both clients
from telethon import TelegramClient, events, functions, types
import asyncio


CHANNEL_IDS = [-1001966404031, -1002495106403] # Replace with your actual channel IDs

async def react_to_message(event, client):
    if event.is_channel:
        try:
            await client(functions.messages.SendReactionRequest(
                peer=event.chat_id,
                msg_id=event.id,
                big=True,
                add_to_recent=True,
                reaction=[types.ReactionEmoji(emoticon='❤️')]
            ))
            print(f"Client reacted to message from {event.chat.title} with ❤️")
            await asyncio.sleep(2)
        except Exception as e:
            print(f"Client Error: {e}")

@client.on(events.NewMessage(chats=CHANNEL_IDS))
async def handler_client1(event):
    await react_to_message(event, event.client)

@client2.on(events.NewMessage(chats=CHANNEL_IDS))
async def handler_client2(event):
    await react_to_message(event, event.client)
if __name__ == "__main__":
    # Initialize your clients here (assuming you have code for this)
    client = TelegramClient(...)  
    client2 = TelegramClient(...)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.start())
    loop.run_until_complete(client2.start())

    # Add your event handlers here
    client.add_event_handler(handler_client1)
    client2.add_event_handler(handler_client2)

    loop.run_forever()
