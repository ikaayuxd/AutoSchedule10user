from .. import client, TIME
from telethon import events, types
import logging 
import asyncio
import random

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('Felling Something Happening')

class temp(object):
    CANCEL = False

channel_ids = [-1001966404031, -1001966404031, -1001966404031]  # Replace with your channel IDs

messages = [
    "hii1",
    "hii2",
    "hii3"
]  # Add your desired messages here

async def forward_messages(client):
    async with client.conversation(channel_ids) as conv:
        while True:
            if temp.CANCEL:
                break
            try:
                response = await conv.get_response()
                for channel_id in channel_ids:
                    message = random.choice(messages)
                    await client.send_message(channel_id, message)
            except Exception as e:
                logger.exception(e)
                continue
            await asyncio.sleep(TIME)

@client.on(events.NewMessage(outgoing=True, pattern='!cancel'))
async def handle_cancel(event):
    temp.CANCEL = True
    msg = await event.respond('Cancelling Auto Message Forwarding...')
    await asyncio.sleep(5)
    await msg.delete()

@client.on(events.NewMessage(outgoing=True, pattern='!start'))
async def handle_start(event):
    temp.CANCEL = False
    if not temp.CANCEL:
        msg = await event.respond("Starting Auto Message Forwarding...")
        await forward_messages(client)
        await asyncio.sleep(5)
        await msg.delete()
