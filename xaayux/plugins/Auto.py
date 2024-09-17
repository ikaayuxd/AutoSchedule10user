from .. import client, DELAY
from telethon import events, types, Button
import logging 
import asyncio
import random
from xaayux.config import channel_ids, messages, DELAY

async def send_messages():
    while True:
        for channel_id in channel_ids:
            message = random.choice(messages)
            await client.send_message(channel_id, message)
        await asyncio.sleep(DELAY)  # Send a message every 30 minutes 
        
@client.on(events.NewMessage(outgoing=True, pattern='!ccancel'))
async def handle_cancel(event):
    await event.respond('Cancelling Auto Message Forwarding...')
    global send_task
    send_task.cancel()

@client.on(events.NewMessage(outgoing=True, pattern='!cstart'))
async def handle_start(event):
    await event.respond("Starting Auto Message Forwarding...")
    global send_task
    send_task = asyncio.create_task(send_messages())

