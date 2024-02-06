from .. import client, TIME
from telethon import events, types
import logging 
import asyncio
import random

folder_name = "Pro Hacking"  # Replace with the name of your folder

message_links = [
    "https://t.me/GrowWithPromo/113", 
    "https://t.me/GrowWithPromo/127"
]  # Add your desired message links here

async def forward_messages():
    while True:
        for message_link in message_links:
            message = await client.get_messages(message_link)
            for dialog in await client.get_dialogs():
                if isinstance(dialog.entity, Channel) and dialog.entity.megagroup and dialog.entity.folder_id == folder_name:
                    await client.send_message(dialog.entity.id, message)
        await asyncio.sleep(60)  # Send a message every 1 minute

@client.on(events.NewMessage(outgoing=True, pattern='!cancel'))
async def handle_cancel(event):
    await event.respond('Cancelling Auto Message Forwarding...')
    global forward_task
    forward_task.cancel()

@client.on(events.NewMessage(outgoing=True, pattern='!start'))
    async def handle_start(event):
        await event.respond("Starting Auto Message Forwarding...")
        global forward_task
        forward_task = asyncio.create_task(forward_messages())
