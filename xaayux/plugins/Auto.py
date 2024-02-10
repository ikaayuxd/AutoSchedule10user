from .. import client, DELAY
from telethon import events, types
import logging 
import asyncio
import random
from xaayux.config import channel_ids, messages, DELAY, group_ids

# Load group IDs from "groups.txt"
with open("groups.txt", "r") as file:
    group_ids = [line.strip() for line in file]

async def send_messages():
    while True:
        for group_id in group_ids:
            try:
                message = random.choice(messages)
                await client.send_message(int(group_id), message)
                await asyncio.sleep(1)
            except Exception as e:
                await client.send_message(5488677608, f"Error sending message to channel {group_id}: {e}")
                # Remove the failed group ID from the file
                with open("groups.txt", "w") as file:
                    file.write('\n'.join([g for g in group_ids if g != group_id]))
                continue
        await asyncio.sleep(15)  # Send a message every 30 minutes

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

logging.basicConfig(level=logging.WARNING)

with client:
    client.run_until_disconnected()
