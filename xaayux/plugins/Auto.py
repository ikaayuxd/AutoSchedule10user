from .. import client, TIME
from telethon import events, types
import logging 
import asyncio
import random

channel_ids = [-1001966404031]  # Replace with your channel IDs

messages = [
    "hii1",
    "hii2",
    "hii3"
]  # Add your desired messages here

async def send_messages():
    while True:
        for channel_id in channel_ids:
            message = random.choice(messages)
            await client.send_message(channel_id, message)
        await asyncio.sleep(60)  # Send a message every 1 minute

@client.on(events.NewMessage(outgoing=True, pattern='!cancel'))
async def handle_cancel(event):
    await event.respond('Cancelling Auto Message Forwarding...')
    global send_task
    send_task.cancel()

@client.on(events.NewMessage(outgoing=True, pattern='!start'))
async def handle_start(event):
    await event.respond("Starting Auto Message Forwarding...")
    global send_task
    send_task = asyncio.create_task(send_messages())
